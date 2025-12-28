from project.python_basic.sets.sets_01 import create_set

def run():
    print("\nCreate a program that receives two sets and returns the elements")
    print("that belong to the first set but not to the second, without repetition.")

    first_set = create_set("first")
    second_set = create_set("second")
    difference_of_sets = first_set.difference(second_set)

    if len(first_set) == 0: first_set.add("∅")
    if len(second_set) == 0: second_set.add("∅")
    if len(difference_of_sets) == 0: difference_of_sets.add("∅")
    print(f"\nThe difference of the sets {first_set} and {second_set} is {difference_of_sets}")