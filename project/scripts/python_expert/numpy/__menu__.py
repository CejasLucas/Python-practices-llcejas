from project.scripts.python_expert.numpy.numpy_01 import run as ex_01
from project.scripts.python_expert.numpy.numpy_02 import run as ex_02
from project.scripts.python_expert.numpy.numpy_03 import run as ex_03
from project.scripts.python_expert.numpy.numpy_04 import run as ex_04

def get_statements_with_numpy_exercises():
    return [
        {"statement": "Matrix operations and slicing", "exercise": ex_01},
        {"statement": "Sum and average of matrix elements", "exercise": ex_02},
        {"statement": "7x9 matrix with column patterns", "exercise": ex_03},
        {"statement": "5x5 random matrix - positions > 0.5", "exercise": ex_04}
    ]
