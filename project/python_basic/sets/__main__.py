from project.python_basic.sets.sets_00 import get_sets_exercises
from project.utils.loader import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n============================== COLLECTIONS PRACTICE SET ==============================")
    builder = ExerciseBuilder(practice=get_sets_exercises())
    builder.run()