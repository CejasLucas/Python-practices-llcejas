from src.main.Practices.sets.exercise1 import create_set
from src.main.Practices.sets.exercise1 import create_list
from src.main.Practices.sets.exercise1 import run_exercise_1
from src.main.Practices.sets.exercise2 import run_exercise_2
from src.main.Practices.sets.exercise3 import run_exercise_3

def run_exercise_4():
    print("\nCreate a program that simplifies working with sets.")
    print("Remember, a set is a collection with no repeated elements.")

    print("\nWrite the number corresponding: ")
    print("(1) Convert List to Set")
    print("(2) Union")
    print("(3) Intersection")
    print("(4) Difference")
    print("(5) Check Equality")

    number = int(input("Enter a number: "))
    examples = {1: convert_to_set , 2: run_exercise_1, 3: run_exercise_2, 4: run_exercise_3, 5: equality}

    if number in examples:
        examples[number]()
    else:
        print("Invalid option. Try again.")

def convert_to_set():
    first_list = create_list("first")
    second_list = create_list("second")
    print(f"\nFirst list before being converted to a set: {first_list}")
    print(f"\nSecond list before being converted to a set: {second_list}")
    print(f"\nFirst list converted to set: {set(first_list)}")
    print(f"\nSecond list converted to set: {set(second_list)}")

def equality():
    first_set = create_set("first")
    second_set = create_set("second")
    validate = first_set == second_set
    print(f"\nAre sets {first_set} and {second_set} equal? The answer is {validate}")