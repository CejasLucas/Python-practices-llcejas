from project.python_basic.tuples.tuples_00 import get_tuples_exercises
from project.utils.loader import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n============================== COLLECTIONS PRACTICE TUPLE ==============================")
    builder = ExerciseBuilder(practice=get_tuples_exercises())
    builder.run()