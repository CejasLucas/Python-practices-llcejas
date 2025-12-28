from project.python_basic.lists import (
    lists_01,
    lists_02,
    lists_03,
    lists_04,
    lists_05,
    lists_06
)

def get_lists_exercises():
    return {
        1: {"name": "Create a list of words and display it", "exercise": lists_01},
        2: {"name": "Count how many times a word appears", "exercise": lists_02},
        3: {"name": "Replace a word in the list", "exercise": lists_03},
        4: {"name": "Remove a word from the list", "exercise": lists_04},
        5: {"name": "Remove from list1 words in list2", "exercise": lists_05},
        6: {"name": "Create a reversed copy of the list", "exercise": lists_06}
    }
