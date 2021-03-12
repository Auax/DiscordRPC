# ~ Main file
"""
Discord Status app created by Zelliux
"""

# Imports
import math
import time
import datetime
from pypresence import Presence, ServerError, InvalidID

from __init__ import *

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
        self.config = util.load_json(config_path)  # Load config.json file

        try:
            # Identifiers
            self.clientID = str(self.config['Identifiers']['clientID'])

            # State
            self.state = str(self.config['State']['state'])
            self.startTimeStamp = int(self.config['State']['startTimeStamp'])

            # Image
            self.largeImage = self.config['Images']['largeImage']
            self.smallImage = self.config['Images']['smallImage']

        except ValueError:
            util.logger("Error", "values types are incorrect", "error")
            raise ValueError

        # Raise an error if the ClientID is not 18
        assert len(self.clientID) == 18 and self.state, "Please fill the correct values"

        # Assign default values
        if not self.largeImage:
            self.largeImage = None
        # Assign default values
        if not self.smallImage:
            self.smallImage = None
        # Assign default values
        if not self.startTimeStamp:
            self.startTimeStamp = 0

    def connect(self) -> None:
        """
        Connect to Discord Rich Presence App
        :return: None
        """
        if self.clientID and self.state:

            # Print parameters
            util.logger("ClientID", self.clientID[:int(len(self.clientID) / 2)] + "...")
            util.logger("State", self.state)

            RPC = Presence(self.clientID)  # Initialize the client class

            try:
                RPC.connect()  # Start the handshake loop

            except Exception as E:
                util.logger("Error",
                            "An error has occurred while trying to connect to Discord. Make sure your Discord client is running!",
                            "error")
                raise E

            util.logger("Connect", True, "success")

            # Set played time
            played_seconds = datetime.timedelta(seconds=self.startTimeStamp)

            # Start Loop
            while True:
                if 2 > played_seconds.days >= 1:
                    display_time = f"playing for {played_seconds.days} day"  # Set display time

                elif 30 > played_seconds.days >= 2:
                    display_time = f"playing for {played_seconds.days} days"  # Set display time

                elif 60 > played_seconds.days >= 30:
                    display_time = "playing for 1 month"  # Set display time
                elif 365 > played_seconds.days >= 60:
                    months = math.floor(played_seconds.days / 30)  # Divide and round down
                    display_time = f"playing for {months} months"  # Set display time

                elif 730 > played_seconds.days >= 365:
                    display_time = "playing for 1 year"  # Set display time

                elif played_seconds.days >= 730:
                    years = math.floor(played_seconds.days / 365)  # Divide and round down
                    display_time = f"playing for {years} years"  # Set display time

                else:
                    display_time = f"{played_seconds} elapsed"  # Set display time

                try:
                    # Update status every second
                    RPC.update(large_image=self.largeImage, details=self.state,
                               state=display_time)
                    played_seconds += datetime.timedelta(seconds=1)

                    time.sleep(1)  # Delay in seconds

                except ServerError:
                    # Log error
                    util.logger("Error", "State value must be at least 2 characters long.", "error")
                    break

                except InvalidID:
                    # Log error
                    util.logger("Error", "Specify a valid client ID.", "error")
                    break

                except Exception as E:
                    util.logger("Error", f"Unexpected error: {col.fore_color(str(E), 'BLUE')}", "error")
                    break

        else:
            # Error message
            util.logger("Error", "Please fill the required values", "error")


# Do the magic
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")  # Clear console

    util.slow_type(""" 
█▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄   █▀█ █ █▀▀ █░█   █▀█ █▀█ █▀▀ █▀ █▀▀ █▄░█ █▀▀ █▀▀
█▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀   █▀▄ █ █▄▄ █▀█   █▀▀ █▀▄ ██▄ ▄█ ██▄ █░▀█ █▄▄ ██▄""", 10)
    util.slow_type("\nDiscord Status Repository by Ibai Farina (2006)", delay=40)
    print("\n" + "-" * 50 + "\n")  # Escape

    try:
        # Initialize class
        dp = DiscordPresence("config.json")
        # Connect to Discord!
        dp.connect()

    except Exception as E:
        print(E)

    print("\n")  # Escape
    util.slow_type(col.fore_color("Press enter to exit...", "MAGENTA"), delay=40)
    input("")
