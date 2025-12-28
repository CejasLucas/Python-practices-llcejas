from project.python_basic.lists.lists_00 import get_lists_exercises
from project.utils.loader import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== COLLECTIONS PRACTICE LIST ===========================")
    builder = ExerciseBuilder(practice=get_lists_exercises())
    builder.run()