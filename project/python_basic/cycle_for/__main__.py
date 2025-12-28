from project.python_basic.cycle_for.cycle_for_00 import get_cycle_for_exercises
from project.utils.loader import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n======================= CYCLE FOR PRACTICE =======================" + Style.RESET_ALL)
    builder = ExerciseBuilder(practice=get_cycle_for_exercises())
    builder.run()