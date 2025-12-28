from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4
from .exercise5 import run_exercise_5
from .exercise6 import run_exercise_6

def get_networkx_exercises():
    return {
        1: {"name": "Dijkstra shortest path (Z to A)", "func": run_exercise_1},
        2: {"name": "Minimal telephone network & analysis", "func": run_exercise_2},
        3: {"name": "Fuel optimization between cities (A to H)", "func": run_exercise_3},
        4: {"name": "Distance analysis between cities", "func": run_exercise_4},
        5: {"name": "Trip to Prague: routes & landmarks", "func": run_exercise_5},
        6: {"name": "Employee computer network analysis", "func": run_exercise_6},
    }
