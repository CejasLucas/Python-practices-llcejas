from src.main.Practices.lists.exercise1 import list_created

def run_exercise_3():
    print("\nCreate a list of words, then ask for two words and replace the first")
    print("(if in the list) with the second. Display the updated list.")

    word_list = list_created()
    first_word = input("\nEnter the word to replace: ")

    if first_word in word_list:
        print(f"\nInitial list: {word_list}")
        word_change(first_word, word_list)
        print(f"\nModified list: {word_list}")
    else:
        print(f"\nThe word '{first_word}' was not found in the list.")


def word_change(first_word, word_list):
    second_word = input("\nEnter the second word: ")
    i = word_list.index(first_word)
    word_list[i] = second_word