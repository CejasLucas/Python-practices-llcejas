from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[4]
DATA_FILE = PROJECT_ROOT / "data" / "cars_database.csv"

def calculated_pandas_df(dataframe):
    dataframe['Price'] = pd.to_numeric(dataframe['Price'], errors='coerce')

    min_price = dataframe['Price'].min()
    max_price = dataframe['Price'].max()
    avr_price = dataframe['Price'].mean()
    min_brands = ", ".join(dataframe.loc[dataframe['Price'] == min_price, 'Brand'].astype(str).values)
    max_brands = ", ".join(dataframe.loc[dataframe['Price'] == max_price, 'Brand'].astype(str).values)

    data = {
        'Price': [min_price, max_price, avr_price],
        'Brand': [min_brands, max_brands, '—']
    }
    return pd.DataFrame(data, index=['Minimum', 'Maximum', 'Average'])


def run_exercise_4():
    print("\nUsing the file autos.xlsx (car prices and stock data) ")
    print("write code to display the minimum, maximum, and average price.")
    print(f"\nSearching for the file at: {DATA_FILE}")

    if not DATA_FILE.exists():
        raise FileNotFoundError(f"\n❌ The file does not exist in: {DATA_FILE}")

    dataframe = pd.read_csv(DATA_FILE, delimiter=";")

    new_dataframe = calculated_pandas_df(dataframe)

    print("\n"+ "=" * 50)
    print(f"{'🚦  cars_database.csv file found':^50}")
    print("=" * 50)
    print(dataframe)
    print("-" * 50)

    print("\n" * 2 + "=" * 50)
    print(f"{'🚗  Car price summary with Pandas DataFrame':^50}")
    print("=" * 50)
    print(new_dataframe)
    print("-" * 50)