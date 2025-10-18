from src.main.Practices.lists.exercise1 import list_created

def run_exercise_4():
    print("\nCreate a list of words, then ask for a word and remove it from the list.")

    word_list = list_created()
    word_to_search = input("\nEnter a word to search for in the list and delete it: ")

    if word_to_search in word_list:
        word_list.remove(word_to_search)
        print(f"T\nhe word '{word_to_search}' was deleted.")
        print(f"\nUpdated list: {word_list}")
    else:
        print(f"\nThe word '{word_to_search}' was not found in the list.")