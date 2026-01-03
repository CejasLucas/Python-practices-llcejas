def run():
    sum = 0
    print("\nKeep asking for numbers until a negative number is entered.")
    print("At the end, print the sum of all entered numbers.")
    while True:
        number = int(input("\nEnter a positive number: "))
        if number <= 0:
            break
        sum += number

    print(f"\nThe sum of the positive numbers is {sum}")