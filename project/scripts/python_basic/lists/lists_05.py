from project.scripts.python_basic.lists.lists_01 import list_created

def run():
    print("\nCreate two lists of words, then remove from the")
    print("first list any words that are also in the second.")

    first_word_list = list_created()
    second_word_list = list_created()

    for word in range(len(first_word_list) - 1, -1, -1):
        if first_word_list[word] in second_word_list:
            del first_word_list[word]

    print("\nUpdated first list (after deletions):")
    print(first_word_list)