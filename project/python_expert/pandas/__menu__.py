from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4
from .exercise5 import run_exercise_5
from .exercise6 import run_exercise_6
from .exercise7 import run_exercise_7

def get_pandas_exercises():
    return {
        1: {"name": "Sales discount calculation", "func": run_exercise_1},
        2: {"name": "Student grades statistics", "func": run_exercise_2},
        3: {"name": "Monthly balance calculation", "func": run_exercise_3},
        4: {"name": "Car prices analysis (autos.xlsx)", "func": run_exercise_4},
        5: {"name": "Internal commerce CSV analysis", "func": run_exercise_5},
        6: {"name": "Grouping and stats on datasets", "func": run_exercise_6},
        7: {"name": "Salary database analysis", "func": run_exercise_7}
    }
