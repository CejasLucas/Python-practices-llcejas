from project.scripts.python_basic.lists.lists_01 import list_created

def run():
    print("\nCreate a list of words, then ask for a word")
    print("and count how many times it appears in the list.")

    count = 0
    create_word_list = list_created()
    word_to_search = input("\nEnter a word to find within the list already created: ")

    for word in create_word_list:
        if word_to_search == word:
            count += 1

    print(create_word_list)
    print(f"\nThe word {word_to_search} is found {count} times")