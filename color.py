from colorama import Fore, Back, init

# Required for CMD. Otherwise colors won't be formatted
init(convert=True)


class Color:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.previous_color = None

    def set_color(self, output_mode: str, text: str, color: str) -> str:
        """
        Change text color
        - output_mode: can either be "fore" or "back" mode
        """

        assert "fore" in output_mode or "back" in output_mode, "Please set either fore or back mode"  # Assert the mode is correctly set
        assert isinstance(text, str) and isinstance(color,
                                                    str), "Specified type is not supported"  # Assert arguments type is correct

        # Assign a mode
        if output_mode == "fore":
            col = getattr(Fore, color)
            mode = Fore

        else:
            col = getattr(Back, color)
            mode = Back

        # Create the colored text
        if self.previous_color:
            c_text = col + text + self.previous_color

        else:
            c_text = col + text + mode.WHITE
            # Set previous color
            self.previous_color = mode.WHITE

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
        return self.set_color("fore", text, color)
