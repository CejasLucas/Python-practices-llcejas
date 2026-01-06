from project.scripts.python_basic.cycle_for.cycle_for_01 import run as ex_01
from project.scripts.python_basic.cycle_for.cycle_for_02 import run as ex_02
from project.scripts.python_basic.cycle_for.cycle_for_03 import run as ex_03
from project.scripts.python_basic.cycle_for.cycle_for_04 import run as ex_04

def get_statements_with_cycle_for_exercises():
    return [
        {"statement": "Print the first 100 natural numbers", "exercise": ex_01},
        {"statement": "Sum the first N odd numbers", "exercise": ex_02},
        {"statement": "Calculate the factorial of a number", "exercise": ex_03},
        {"statement": "Display the first N numbers of the Fibonacci sequence", "exercise": ex_04}
    ]
