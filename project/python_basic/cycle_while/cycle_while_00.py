from project.python_basic.cycle_while import (
    cycle_while_01,
    cycle_while_02,
    cycle_while_03,
    cycle_while_04,
    cycle_while_05,
    cycle_while_06,
    cycle_while_07,
    cycle_while_08
)

def get_cycle_while_exercises():
    return {
        1: {"name": "Enter a specified amount of positive numbers", "exercise": cycle_while_01},
        2: {"name": "Enter a second number greater than the first", "exercise": cycle_while_02},
        3: {"name": "Keep entering decimals greater than the first", "exercise": cycle_while_03},
        4: {"name": "Keep entering increasingly larger integers", "exercise": cycle_while_04},
        5: {"name": "Enter numbers until a negative is entered, then sum them", "exercise": cycle_while_05},
        6: {"name": "Enter numbers until their sum exceeds a given limit", "exercise": cycle_while_06},
        7: {"name": "Enter numbers between two values until one is outside the range", "exercise": cycle_while_07},
        8: {"name": "Enter even numbers while choosing to continue", "exercise": cycle_while_08},
    }
