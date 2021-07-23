from colorama import Fore, Back, init, Style
import sys

convert = True if sys.platform == "win32" else False
init(convert=convert, autoreset=True)  # Autoreset color after printing


class Color:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def set_color(self, output_mode: str, text: str, color: str) -> str:
        """
        Change text color
        - output_mode: can either be "fore" or "back" mode
        """

        # Assert the mode is correctly set
        assert "fore" in output_mode or "back" in output_mode, "Please set either 'fore' or 'back' mode"
        # Assert argument types are correct
        assert isinstance(text, str) and isinstance(color, str), "Specified type is not supported"

        # Assign a mode
        if output_mode == "fore":
            col = getattr(Fore, color)

        else:
            col = getattr(Back, color)

        # Create the colored text
        c_text = col + text + Style.RESET_ALL

        # Print colored text
        if self.verbose:
            print(c_text)

        return c_text

    def fore_color(self, text: str, color: str) -> str:
        """
        Change Fore text color
        """
        return self.set_color("fore", text, color)

    def back_color(self, text: str, color: str) -> str:
        """
        Change background text color
        """
        return self.set_color("back", text, color)
