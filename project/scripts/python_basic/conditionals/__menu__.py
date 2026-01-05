from project.scripts.python_basic.conditionals.conditionals_01 import run as ex_01
from project.scripts.python_basic.conditionals.conditionals_02 import run as ex_02
from project.scripts.python_basic.conditionals.conditionals_03 import run as ex_03
from project.scripts.python_basic.conditionals.conditionals_04 import run as ex_04
from project.scripts.python_basic.conditionals.conditionals_05 import run as ex_05
from project.scripts.python_basic.conditionals.conditionals_06 import run as ex_06

def get_statements_with_conditional_exercises():
    return  [
        {"statement": "Find the Smaller Number", "exercise": ex_01},
        {"statement": "Day of the Week", "exercise": ex_02},
        {"statement": "Voting System", "exercise": ex_03},
        {"statement": "Check for Vowel", "exercise": ex_04},
        {"statement": "Leap Year", "exercise": ex_05},
        {"statement": "Students of an Institute", "exercise": ex_06}
    ]
