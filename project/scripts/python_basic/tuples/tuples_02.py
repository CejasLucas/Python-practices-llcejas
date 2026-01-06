import random

def run():

    print("\nCreate a tuple with predefined values from 1 to 40.")
    print("Ask the user for an index and display the corresponding value from the tuple.")
    number = int(input("\nEnter a positive index from 1 to 40: "))

    if -1 < number < 40:
        numbers = tuple(random.randint(1, 10) for _ in range(41))

        print(f"\nNumber of printed element {len(numbers)}")

        print(f"\nRandomly created tuple: {numbers}")

        print(f"\nThe number at index of the tuple is [{number}] = {numbers[number]}")

    else:
        print("\nYou entered a number outside the range.")