from project.python_basic.cycle_for import (
    cycle_for_01,
    cycle_for_02,
    cycle_for_03,
    cycle_for_04
)

def get_cycle_for_exercises():
    return {
        1: {"name": "Print the first 100 natural numbers", "exercise": cycle_for_01},
        2: {"name": "Sum the first N odd numbers", "exercise": cycle_for_02},
        3: {"name": "Calculate the factorial of a number", "exercise": cycle_for_03},
        4: {"name": "Display the first N numbers of the Fibonacci sequence", "exercise": cycle_for_04},
    }
