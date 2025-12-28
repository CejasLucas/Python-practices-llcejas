from project.python_basic.dictionaries.dictionaries_00 import get_dictionaries_exercises
from project.utils.loader import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n================================== COLLECTIONS PRACTICE: DICTIONARIES ==================================")
    builder = ExerciseBuilder(practice=get_dictionaries_exercises())
    builder.run()