from project.scripts.python_basic.cycle_while.cycle_while_01 import run as ex_01
from project.scripts.python_basic.cycle_while.cycle_while_02 import run as ex_02
from project.scripts.python_basic.cycle_while.cycle_while_03 import run as ex_03
from project.scripts.python_basic.cycle_while.cycle_while_04 import run as ex_04
from project.scripts.python_basic.cycle_while.cycle_while_05 import run as ex_05
from project.scripts.python_basic.cycle_while.cycle_while_06 import run as ex_06
from project.scripts.python_basic.cycle_while.cycle_while_07 import run as ex_07
from project.scripts.python_basic.cycle_while.cycle_while_08 import run as ex_08

def get_statements_with_cycle_while_exercises():
    return [
        {"statement": "Enter a specified amount of positive numbers", "exercise": ex_01},
        {"statement": "Enter a second number greater than the first", "exercise": ex_02},
        {"statement": "Keep entering decimals greater than the first", "exercise": ex_03},
        {"statement": "Keep entering increasingly larger integers", "exercise": ex_04},
        {"statement": "Enter numbers until a negative is entered, then sum them", "exercise": ex_05},
        {"statement": "Enter numbers until their sum exceeds a given limit", "exercise": ex_06},
        {"statement": "Enter numbers between two values until one is outside the range", "exercise": ex_07},
        {"statement": "Enter even numbers while choosing to continue", "exercise": ex_08}
    ]
