def run():
    print("Ask the user for a year and determine if it’s a leap year")
    print("(divisible by 4 and not 100, unless also divisible by 400).")
    year_input = input("\nEnter a year: ")
    try:
        year = int(year_input.strip())
    except ValueError:
        print("\n❌ Invalid input: please enter a valid number.\n")
        return

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"\n✅ The year {year} is a Leap Year.\n")
    else:
        print(f"\n❌ The year {year} is not a Leap Year.\n")
    return
