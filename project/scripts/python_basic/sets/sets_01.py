def run():
    print("\nCreate a program that receives two sets and")
    print("returns the common elements between them, without repetition.")

    first_set = create_set("first")
    second_set = create_set("second")
    intersection_of_sets = first_set.intersection(second_set)

    if len(first_set) == 0: first_set.add("∅")
    if len(second_set) == 0: second_set.add("∅")
    if len(intersection_of_sets) == 0: intersection_of_sets.add("∅")
    print(f"\nThe intersection of the sets {first_set} and {second_set} is {intersection_of_sets}")


def create_set(feature):
    i = 0
    new_set = set()
    print("\nNOTE: Enter a * each time you want to stop entering items")
    while True:
        element = input(f"\nEnter element {i} for the {feature} set: ")
        if element == "*":
            print("\nCutting condition executed.\n")
            break
        i += 1
        new_set.add(element)
    return new_set

def create_list(feature):
    i = 0
    new_list = list()
    print("\nNOTE: Enter a * each time you want to stop entering items")
    while True:
        element = input(f"\nEnter index {i} for the {feature} list: ")
        if element == "*":
            print("\nCutting condition executed.\n")
            break
        i += 1
        new_list.append(element)
    return new_list