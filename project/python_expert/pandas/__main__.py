from src.main.Practices.__loader__ import ExerciseBuilder
from src.main.Practices.utils_pandas.__menu__ import get_pandas_exercises
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_pandas_exercises().items()}
    submenu = {k: v["name"] for k, v in get_pandas_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== PANDAS PRACTICE MENU ===========================")

    builder = ExerciseBuilder(exercises=exercises, menu = submenu)
    builder.run()