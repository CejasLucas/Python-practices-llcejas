from .exercise1 import run_exercise_1
from .exercise2 import run_exercise_2
from .exercise3 import run_exercise_3
from .exercise4 import run_exercise_4
from .exercise5 import run_exercise_5
from .exercise6 import run_exercise_6
from .exercise7 import run_exercise_7
from .exercise8 import run_exercise_8
from .exercise9 import run_exercise_9
from .exercise10 import run_exercise_10

def get_venn_diagrams_exercises():
    return {
        1: {"name": "Basic Set Operations in Python", "func": run_exercise_1},
        2: {"name": "Language Study Venn Diagram", "func": run_exercise_2},
        3: {"name": "Algebra II and Sports Participation", "func": run_exercise_3},
        4: {"name": "M, N and Universe U Analysis", "func": run_exercise_4},
        5: {"name": "Tech Ownership among Students", "func": run_exercise_5},
        6: {"name": "Cardinalities from Venn Diagram", "func": run_exercise_6},
        7: {"name": "Pet Ownership Survey", "func": run_exercise_7},
        8: {"name": "Transportation in Buenos Aires", "func": run_exercise_8},
        9: {"name": "Family Educational Levels", "func": run_exercise_9},
        10: {"name": "Students in Math, Physics & Chemistry", "func": run_exercise_10}
    }