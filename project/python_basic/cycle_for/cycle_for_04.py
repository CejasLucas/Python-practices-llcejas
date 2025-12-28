def run():
    x, y, z = 1, 1, 1
    fibonacci_sequence = []
    print("\nAsk for a number N and display the first N numbers of the Fibonacci sequence.")
    test_number = int(input("\nEnter a number to calculate: "))
    if test_number > 0:
        for number in range(test_number):
            z = x + y
            y = x
            x = z
            fibonacci_sequence.append(x)
        print("\nFor the number N the following Fibonacci sequence was created")
        print(fibonacci_sequence)
    else:
        print("\nNegative numbers are not allowed")