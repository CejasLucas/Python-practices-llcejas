def run():
    print("\nAsk for integers while the user keeps entering larger numbers.")
    print("Print the previous number each time. Stop when a smaller number is entered.")
    previous_number = float(input("\nEnter a decimal number: "))
    list_of_numbers = [previous_number]

    while True:
        last_number = float(input("\nEnter a decimal number: "))
        list_of_numbers.append(last_number)
        if last_number < previous_number:
            break
        previous_number = last_number

    last_number = list_of_numbers.pop()
    print(f"\nThe last number was less than to the previous. Cut number was = {last_number}")
    print(f"\nList of exponential numbers: {list_of_numbers}")