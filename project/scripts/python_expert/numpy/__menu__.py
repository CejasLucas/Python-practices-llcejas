from scripts.python_expert.numpy import numpy_03, numpy_01, numpy_02, numpy_04


def get_statements_with_numpy_exercises():
    return [
        {"statement": "Matrix operations and slicing", "exercise": numpy_01},
        {"statement": "Sum and average of matrix elements", "exercise": numpy_02},
        {"statement": "7x9 matrix with column patterns", "exercise": numpy_03},
        {"statement": "5x5 random matrix - positions > 0.5", "exercise": numpy_04}
    ]
