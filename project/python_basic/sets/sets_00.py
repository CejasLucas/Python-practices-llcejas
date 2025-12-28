from project.python_basic.sets import (
    sets_01,
    sets_02,
    sets_03,
    sets_04
)

def get_sets_exercises():
    return {
        1: {"name": "Intersection of sets", "exercise": sets_01},
        2: {"name": "Union of sets", "exercise": sets_02},
        3: {"name": "Difference of sets", "exercise": sets_03},
        4: {"name": "Set operations toolkit", "exercise": sets_04},
    }
