"""
Python Discord Status
----------------------
By Ibai Farina
The version 1.2 Adds new functionallity and a refactor of some files.
Discord-Status-v1.2 lets you add buttons to your RPC.
"""

__title__ = 'Discord-Status'
__author__ = 'Ibai Farina'
__license__ = 'MIT'
__version__ = '1.2'

import datetime
import json
import os
import random
import sys
import time

from pypresence import Presence, ServerError, InvalidID, exceptions
from misc import color, logger, date

col = color.Color()


class DiscordPresence:
    """
    Set Discord Presence Class
    """

    def __init__(self, config_path: str):
        """
        Init config
        :param config_path: the path to config.json
        """
        # Load config.json file
        with open(config_path, encoding="utf8") as file:
            self.config = json.load(file)
            file.close()

        try:
            # Identifier ID
            self.client_id_ = str(self.config['Identifiers']['clientID'])

            # State
            self.state = str(self.config['State']['state'])
            self.startTimeStamp = int(self.config['State']['startTimeStamp'])
            # If state is null then use the sequence
            self.state_seq = self.config["State"]["stateRndSeq"]
            # Whether track running time
            self.use_time = int(self.config['State']['useTime'])
            # The sleeping time between each status update in seconds
            self.interval_time = int(self.config['State']['intervalTime'])
            self.buttons = self.config["State"]["buttons"]
            if self.buttons:
                assert len(self.buttons) <= 2, logger.logger("Error", "Max number of buttons is two!", "error")

            # Images
            self.largeImage = self.config['Images']['largeImage']
            self.smallImage = self.config['Images']['smallImage']

        except ValueError:
            logger.logger("Error", "value types are incorrect", "error")
            raise ValueError

        # Raise an error if the length ClientID is not 18
        assert len(self.client_id_) == 18 and self.state, "Please fill the correct values"

        # Assign default time stamp if it's none
        if not self.startTimeStamp:
            self.startTimeStamp = 0

    @property
    def client_id(self):
        return self.client_id_

    def connect(self) -> None:
        """
        Connect to Discord RPC
        :return: None
        """
        if self.client_id and self.state:

            # Log params to the console
            logger.logger("ClientID", self.client_id[:int(len(self.client_id) / 2)] + "...")
            if self.state == "None":
                logger.logger("State sequence", ",".join(self.state_seq))
            else:
                logger.logger("State", self.state)

            rpc = Presence(self.client_id)  # Initialize RPC

            try:
                rpc.connect()  # Start the handshake loop
                logger.logger("Connect", "true", "success")

            except exceptions.InvalidPipe:
                logger.logger("Error",
                              "An error has occurred while trying to connect to Discord. Make sure your Discord "
                              "client is running!",
                              "error")
                sys.exit(-1)

            # Set initial played time
            played_seconds = datetime.timedelta(seconds=self.startTimeStamp)

            # Start Loop
            while True:
                display_time = date.format_date(played_seconds) if self.use_time else "  "

                try:
                    # Update status every second
                    if self.state == "None":
                        iter_state = random.choice(self.state_seq)

                    else:
                        iter_state = self.state

                    rpc.update(large_image=self.largeImage,
                               small_image=self.smallImage,
                               details=iter_state,
                               state=display_time,
                               buttons=self.buttons)

                    played_seconds += datetime.timedelta(seconds=1)
                    time.sleep(self.interval_time)  # Delay in seconds

                except ServerError as E:
                    logger.logger("Error", f"ServerError: {E}", "error")
                    break

                except InvalidID:
                    logger.logger("Error", "Connection closed. Possible cause: Invalid ID", "error")
                    break

                except Exception as E:
                    logger.logger("Error", f"Unexpected error: {col.fore_color(str(E), 'BLUE')}", "error")
                    break

        else:
            logger.logger("Error", "Please fill the required values", "error")


# Do the magic
if __name__ == "__main__":
    try:
        os.system("cls" if os.name == "nt" else "clear")  # Clear console

        # print(pyfiglet.figlet_format("Alpha sniper", font="big"))
        print("Zellius")
        print("-" * 50 + "\n")  # Escape

        try:
            # Initialize class
            dp = DiscordPresence("config.json")
            # Connect to Discord
            dp.connect()

        except FileNotFoundError:
            logger.logger("Error", "config.json file not found. Make sure it's in the same directory.",
                          "error")

        except Exception as E:
            logger.logger("Error", f"Unexpected error: {col.fore_color(str(E), 'WHITE')}", "error")

    except KeyboardInterrupt:
        pass

    except Exception as E:
        input(E)

    finally:
        print(col.fore_color("\nExiting...", "RED"))
        input("Exit? >> ")
        sys.exit(-1)
