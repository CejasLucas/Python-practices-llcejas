def run():
    list_of_numbers = []
    print("\nAsk for two integers (min and max).")
    print("Then keep asking for numbers between them.")
    print("Stop when a number outside the range is entered.")
    print("Print how many valid numbers were entered.")
    while True:
        min = float(input("\nEnter the minimum of the range: "))
        max = float(input("\nEnter the maximum of the range: "))
        if min > max:
            print("\nThe maximum must be greater than the minimum.")
        else:
            print(f"\nPerfect, your range is the following [{min},{max}]")
            break

    while True:
        number = float(input("\nEnter a number: "))
        if min < number < max:
            list_of_numbers.append(number)
        else:
            break

    print(f"\nList of numbers within the established range [{min},{max}]")
    print(list_of_numbers)