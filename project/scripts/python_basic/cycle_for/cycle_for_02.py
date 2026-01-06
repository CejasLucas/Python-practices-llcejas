def run():
    sum = 0
    odd_numbers = []
    print("\nAsk the user for a number N, then calculate")
    print("the sum of the first N odd numbers.")
    stop = int(input("\nEnter a number: "))
    for number in range(0,stop):
        if number % 2 != 0:
            odd_numbers.append(number)
            sum += number

    print(f"\nList odd numbers found: {odd_numbers}")
    print(f"\nThe sum of the first N = {stop} numbers is {sum}")