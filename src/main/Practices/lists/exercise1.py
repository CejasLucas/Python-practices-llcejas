def run_exercise_1():
    print("\nCreate a list of words by entering a number and then that many words.")
    print("Finally, display the list.")
    word_list = list_created()

    print("\nList of created words:")
    print(word_list)

def list_created():
    word_list = []
    number = int(input("\nEnter the number of items to load: "))
    for i in range(number): word_list.append(input(f"\nEnter item {i + 1}: "))

    return word_list