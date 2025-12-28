from src.main.Practices.utils_venn_diagrams.__menu__ import get_venn_diagrams_exercises
from src.main.Practices.__loader__ import ExerciseBuilder
from colorama import Fore, Style

if __name__ == "__main__":
    exercises = {k: v["func"] for k, v in get_venn_diagrams_exercises().items()}
    submenu = {k: v["name"] for k, v in get_venn_diagrams_exercises().items()}
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\n================== VENN DIAGRAMS PRACTICE ==================" + Style.RESET_ALL)

    builder = ExerciseBuilder(exercises=exercises, menu=submenu)
    builder.run()