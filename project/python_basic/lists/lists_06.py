from project.python_basic.lists.lists_01 import list_created

def run():
    print("\nCreate a list of words, then create a second")
    print("list that is the reverse of the first (as a separate list).")

    second_word_list = []
    first_word_list = list_created()

    for i in range(len(first_word_list) - 1, -1, -1):
        second_word_list.append(first_word_list[i])

    print("\nOriginal list:")
    print(first_word_list)

    print("\nReversed list:")
    print(second_word_list)