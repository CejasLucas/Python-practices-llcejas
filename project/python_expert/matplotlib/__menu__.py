from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4
from .exercise5 import run_exercise_5
from .exercise6 import run_exercise_6

def get_matplotlib_exercises():
    return {
        1: {"name": "Bar chart of Latin American GDP (2019)", "func": run_exercise_1},
        2: {"name": "GDP percentage pie chart", "func": run_exercise_2},
        3: {"name": "Scatter plot: population vs. surface", "func": run_exercise_3},
        4: {"name": "Grouped bar chart of product outputs", "func": run_exercise_4},
        5: {"name": "Stacked bar chart: beverage consumption", "func": run_exercise_5},
        6: {"name": "Scatter plot: athlete group scores", "func": run_exercise_6},
    }
