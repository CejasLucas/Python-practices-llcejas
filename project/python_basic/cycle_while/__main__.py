from project.python_basic.cycle_while.cycle_while_00 import get_cycle_while_exercises
from project.utils.loader import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n========================= WHILE CYCLE PRACTICE =========================" + Style.RESET_ALL)
    builder = ExerciseBuilder(practice=get_cycle_while_exercises())
    builder.run()