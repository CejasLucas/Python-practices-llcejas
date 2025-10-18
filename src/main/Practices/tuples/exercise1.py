import random

def run_exercise_1():
    print("\nCreate a tuple with numbers. Prompt the user for a number")
    print("and indicate how many times it repeats in the tuple.")
    number = int(input("\nEnter a positive number from [1,50]: "))

    numbers = tuple(random.randint(1, 50) for _ in range(100))

    print(f"\nRandomly created tuple: {numbers}")

    print(f"\nThe entered number '{number}' is repeated within the tuple {numbers.count(number)} times")