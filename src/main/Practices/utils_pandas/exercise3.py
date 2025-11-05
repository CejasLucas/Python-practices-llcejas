import pandas as pd

financial_data = {
    'Month': [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ],
    'Sales': [
        30500, 35600, 28300, 33900, 41000, 45000,
        47000, 52000, 50500, 61500, 63200, 59800
    ],
    'Expenses': [
        22000, 23400, 18100, 20700, 25000, 26000,
        27500, 29500, 28800, 31000, 32500, 31800
    ]
}


def run_exercise_3():
    print("\nWrite a function that receives a DataFrame with sales")
    print("and expenses data and a list of months, and returns the")
    print("total balance (sales − expenses) for the given months.")

    # Create DataFrame from the financial data
    dataframe = pd.DataFrame(financial_data)

    # Display the original DataFrame
    print("\n" * 2 + "=" * 45)
    print(f"{'🏛️  Original DataFrame:':^45}")
    print("=" * 45)
    print(dataframe)
    print("-" * 45)

    # Calculate the monthly balance (Sales - Expenses)
    dataframe['Balance'] = dataframe['Sales'] - dataframe['Expenses']

    # Display the updated DataFrame with the balance
    print("\n" * 2 + "=" * 45)
    print(f"{'⚖️  DataFrame with Monthly Balance':^45}")
    print("=" * 45)
    print(dataframe)
    print("-" * 45)