import pandas as pd

def run_exercise_1():
    print("\nWrite a program that asks the user for sales data over")
    print("a range of years and displays a series indexed by year, ")
    print("showing the sales before and after applying a 10% discount.")

    try:
        start_year = int(input("📈  Enter the first year of sales: "))
        last_year = int(input("📉  Enter the last year of sales: "))

        if last_year < start_year:
            print("❌ The last year cannot be earlier than the starting year.")
            return

        sales = {}
        print("\n" + "=" * 45)
        for year in range(start_year, last_year + 1):
            while True:
                try:
                    total = float(input(f"🔂  Enter total sales for year {year}: "))
                    if total < 0:
                        print("🚫  Sales cannot be negative. Please try again.")
                        continue
                    sales[year] = total
                    break
                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.")
        print("=" * 45 + "\n")

        # Create pandas series
        sales_series = pd.Series(sales, name="Sales")
        discounted_sales_series = sales_series * 0.9  # Apply 10% discount

        # Display results
        print("\n🗓️  Sales by year:")
        print(sales_series)

        print("\n💸  Sales with 10% discount:")
        print(discounted_sales_series)

    except ValueError:
        print("❌ Please enter valid numeric values for the years.")