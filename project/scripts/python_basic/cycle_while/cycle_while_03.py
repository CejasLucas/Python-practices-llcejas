def run():
    print("\nAsk for decimal numbers while the user")
    print("enters values greater than the first one.")
    first_number = float(input("\nEnter a decimal number: "))
    list_of_numbers = [first_number]

    while True:
        last_number = float(input("\nEnter a decimal number: "))
        list_of_numbers.append(last_number)
        if last_number < first_number:
            break

    last_number = list_of_numbers.pop()
    print(f"\nThe last number is less than the first. Cut number was = {last_number}")
    print(f"\nList of entered numbers greater than the first: {list_of_numbers}")