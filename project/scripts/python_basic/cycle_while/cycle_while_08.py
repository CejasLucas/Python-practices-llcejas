def run():
    list_of_numbers = []
    print("\nAsk for even numbers while the user wants to continue.")
    while True:
        number = int(input("\nEnter an even number: "))
        if number % 2 == 0:
            print(f"\nGreat, the number {number} is even")
            list_of_numbers.append(number)
        else:
            print(f"\nThis is an odd number {number}")
            break
    print(f"\nList of entered even numbers: {list_of_numbers}")
