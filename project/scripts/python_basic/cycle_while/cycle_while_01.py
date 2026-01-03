def run():
    count = 0
    list_of_numbers = []
    print("\nAsk how many positive numbers the user must enter.")
    print("Then keep asking for numbers until that amount is reached.")

    test_number = int(input("\nEnter how many numbers you want to load (between 1 and 100): "))

    if 0 < test_number <= 100:
        while count < test_number:
            number = int(input(f"\nEnter a number for index [{count}]: "))
            list_of_numbers.append(number)
            count += 1
        print(f"\nList of numbers created: {list_of_numbers}")
    else:
        print("\nInvalid input. The number must be between 1 and 100.")