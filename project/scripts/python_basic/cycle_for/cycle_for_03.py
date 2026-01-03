def run():
    print("\nAsk the user for a number and calculate its factorial.")
    test_number = int(input("\nEnter a number to calculate: "))
    if test_number < 0:
        print("\nThere is no factorial of a negative number")
    elif test_number < 2:
        print(f"\nThe factorial of '{test_number}' is 1")
    else:
        product = 1
        for number in range(1, test_number + 1): product *= number
        print(f"\nThe factorial of N = '{test_number}' is {product}")