from project.scripts.python_basic.lists.lists_01 import run as ex_01
from project.scripts.python_basic.lists.lists_02 import run as ex_02
from project.scripts.python_basic.lists.lists_03 import run as ex_03
from project.scripts.python_basic.lists.lists_04 import run as ex_04
from project.scripts.python_basic.lists.lists_05 import run as ex_05
from project.scripts.python_basic.lists.lists_06 import run as ex_06

def get_statements_with_lists_exercises():
    return [
        {"statement": "Create a list of words and display it", "exercise": ex_01},
        {"statement": "Count how many times a word appears", "exercise": ex_02},
        {"statement": "Replace a word in the list", "exercise": ex_03},
        {"statement": "Remove a word from the list", "exercise": ex_04},
        {"statement": "Remove from list1 words in list2", "exercise": ex_05},
        {"statement": "Create a reversed copy of the list", "exercise": ex_06}
    ]
