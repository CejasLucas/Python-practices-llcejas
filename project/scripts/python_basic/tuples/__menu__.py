from project.scripts.python_basic.tuples.tuples_01 import run as ex_01
from project.scripts.python_basic.tuples.tuples_02 import run as ex_02
from project.scripts.python_basic.tuples.tuples_03 import run as ex_03

def get_statements_with_tuples_exercises():
    return [
        {"statement": "Count occurrences in a tuple", "exercise": ex_01},
        {"statement": "Get value from tuple by index", "exercise": ex_02},
        {"statement": "Passenger and destination queries", "exercise": ex_03}
    ]
