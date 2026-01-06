from project.scripts.python_basic.sets.sets_01 import run as ex_01
from project.scripts.python_basic.sets.sets_02 import run as ex_02
from project.scripts.python_basic.sets.sets_03 import run as ex_03
from project.scripts.python_basic.sets.sets_04 import run as ex_04

def get_statements_with_sets_exercises():
    return [
        {"statement": "Intersection of sets", "exercise": ex_01},
        {"statement": "Union of sets", "exercise": ex_02},
        {"statement": "Difference of sets", "exercise": ex_03},
        {"statement": "Set operations toolkit", "exercise": ex_04}
    ]
