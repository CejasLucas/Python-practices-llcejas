from colorama import Fore, Style
from project.utils.loader import ExerciseBuilder
from project.python_basic.conditionals.conditionals_00 import get_conditionals_exercises

if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n========== CONDITIONALS PRACTICE ==========")
    builder = ExerciseBuilder(practice=get_conditionals_exercises())
    builder.run()