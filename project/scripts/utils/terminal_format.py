class TerminalFormat:
    def __init__(self):
        pass

    @staticmethod
    def align_left(text: str, width: int = 50): return text.ljust(width)

    @staticmethod
    def align_right(text: str, width: int = 50): return text.rjust(width)

    @staticmethod
    def align_center(text: str, width: int = 50): return text.center(width)

    @staticmethod
    def number_of_spaces(number:int = 1): print("\n" * number)

    @staticmethod
    def line(char: str = "-", length: int = 40): print(char * length)

    @staticmethod
    def line_with_jump(char: str = "-", length: int = 40): print("\n" + char * length)

    def title(self, text: str, char: str = "-", length: int = 60):
        self.number_of_spaces()
        print(char * length)
        print(text.center(length))
        print(char * length)