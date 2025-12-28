from src.main.Practices.utils_matplotlib.__menu__ import get_matplotlib_exercises
from src.main.Practices.__loader__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_matplotlib_exercises().items()}
    submenu = {k: v["name"] for k, v in get_matplotlib_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n=========================== MATPLOTLIB PRACTICE MENU ===========================")

    builder = ExerciseBuilder(exercises=exercises, menu=submenu)
    builder.run()