from project.utils.__terminal_format__ import TerminalFormat

fruits_per_kilogram = {
    "apple": 1000,
    "melon": 2000,
    "mango": 3000,
    "banana": 1000,
    "orange": 2000,
    "pineapple": 3000,
    "blueberry": 6000,
    "strawberry": 5000
}

def run():
    print("\nCreate a dictionary to store fruit prices.")
    print("The program will ask for the fruit name and quantity sold,")
    print("then calculate and display the total price.")

    print("\nIf the fruit is not in the dictionary, an error will be shown.")
    print("After each query, the user will be asked whether they want to continue.")

    text = (TerminalFormat.align_left("Fruit", 20) +
             TerminalFormat.align_center("Price per Kilogram", 40) )

    TerminalFormat().title(text, "=", 55)
    for fruit, price in fruits_per_kilogram.items(): print(f"{fruit.capitalize():<16} | {price:>7} units")
    TerminalFormat.line("=", 55)

    while True:
        fruit_name = input("\n↪️  Enter the name of the fruit: ").strip().lower()

        if fruit_name not in fruits_per_kilogram:
            print("\n🚫  That fruit is not in the list. Please try again.")
            TerminalFormat.line("-", 55)
            TerminalFormat.number_of_spaces()
            break

        try:
            fruit_kilogram = float(input("\n↪️  Enter the number of kilos sold of that fruit: "))
        except ValueError:
            print("\n🚫  Invalid input. Please enter a numeric value for kilograms.")
            TerminalFormat.line("-", 55)
            TerminalFormat.number_of_spaces()
            break

        if fruit_kilogram < 0:
            print("\n🚫  Kilograms cannot be negative.")
            TerminalFormat.line("-", 55)
            TerminalFormat.number_of_spaces()
            break

        price_per_kilogram = fruits_per_kilogram[fruit_name]
        total_price = price_per_kilogram * fruit_kilogram

        print(f"\n📝  The total price for {fruit_kilogram:.2f} kg of {fruit_name} is: {total_price:.2f} units.")
        TerminalFormat.line("-", 80)