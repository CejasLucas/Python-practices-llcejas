from src.main.Practices.lists.exercise1 import list_created

def run_exercise_6():
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