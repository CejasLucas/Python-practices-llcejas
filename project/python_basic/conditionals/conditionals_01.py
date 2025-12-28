def run():
    print("\nEnter two numbers and display the smaller one.")
    x_input = input("Please enter the first number: ")
    y_input = input("Please enter the second number: ")

    try:
        x = float(x_input.strip())
        y = float(y_input.strip())
    except ValueError:
        print("\n❌ Invalid input: make sure to type numbers only.")
        return

    print("\n🔎  Comparing the two numbers...")

    if x < y:
        print(f"\n✅  Result: {x} is smaller than {y}.")
    elif y < x:
        print(f"\n✅  Result: {y} is smaller than {x}.")
    else:
        print(f"\n✅  Result: both numbers are equal ({x}).")
    return
