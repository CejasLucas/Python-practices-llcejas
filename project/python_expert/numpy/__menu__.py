from src.main.Practices.utils_numpy.exercise1 import run_exercise_1
from src.main.Practices.utils_numpy.exercise2 import run_exercise_2
from src.main.Practices.utils_numpy.exercise3 import run_exercise_3
from src.main.Practices.utils_numpy.exercise4 import run_exercise_4

def get_numpy_exercises():
    return {
        1: {"name": "Matrix operations and slicing", "func": run_exercise_1},
        2: {"name": "Sum and average of matrix elements", "func": run_exercise_2},
        3: {"name": "7x9 matrix with column patterns", "func": run_exercise_3},
        4: {"name": "5x5 random matrix - positions > 0.5", "func": run_exercise_4},
    }
