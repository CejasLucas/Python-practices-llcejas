import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def title_center_text(text, number): return print(f"{f'{text}':^{number}}")

def number_of_spaces(number): return print('\n' * number)

def space_with_delimiter(number, delimiter): return print(delimiter * number)

def print_ordered_provinces(series):
    provinces_sorted = series.sort_index()

    number_of_spaces(1)
    space_with_delimiter(50, '=')
    title_center_text("PROVINCES ORDERED ALPHABETICALLY ", 50)
    space_with_delimiter(50, '=')
    for i, (prov, val) in enumerate(provinces_sorted.items(), 1): print(f"{i:02d}. {prov:<25} {val:,.2f}")
    space_with_delimiter(50, '-')


def return_province_values(dataframe):
    dataframe['valor'] = pd.to_numeric(dataframe['valor'], errors='coerce')
    df = dataframe[(dataframe['alcance_tipo'] == 'PROVINCIA') & (dataframe['alcance_nombre'] != 'INDETERMINADA')]
    # This is a Series because it's the result of grouping by 'alcance_nombre' and summing only the 'valor' column

    total_by_province = df.groupby('alcance_nombre')['valor'].sum()
    total_by_province = total_by_province.sort_values(ascending=True)
    print_ordered_provinces(total_by_province)
    return total_by_province


def chart_of_values_by_province(dataframe):
    plt.figure(figsize=(14, 8))
    sns.barplot(x=dataframe.values, y=dataframe.index, palette="magma", legend=False)
    plt.gcf().canvas.manager.set_window_title("Exercise 5")
    plt.title('Total employment by province (sorted)')
    plt.xlabel('Total employment value')
    plt.ylabel('Province')
    plt.tight_layout()
    plt.show()


def data_printing(dataframe):
    print(f"🔁  Number of records uploaded: {dataframe.size}")
    print(f"🔂  Dataframe dimensions: {dataframe.ndim}")

    number_of_spaces(1)
    space_with_delimiter(50, '=')
    title_center_text("COLUMN NAMES", 50)
    space_with_delimiter(50, '=')
    for i, col in enumerate(dataframe.columns): print(f"Column[{i}] {col}")
    space_with_delimiter(50, '-')

    number_of_spaces(1)
    space_with_delimiter(50, '=')
    title_center_text("COLUMN TYPES", 50)
    space_with_delimiter(50, '=')
    print(dataframe.dtypes)
    space_with_delimiter(50, '-')

    number_of_spaces(1)
    space_with_delimiter(140, '=')
    title_center_text("FIRST 5 ROWS OF THE DATA FRAME", 140)
    space_with_delimiter(140, '=')
    print(dataframe.head(5))


    number_of_spaces(1)
    space_with_delimiter(140, '=')
    title_center_text("LAST 5 ROWS OF THE DATA FRAME", 140)
    space_with_delimiter(140, '=')
    print(dataframe.tail(5))
    number_of_spaces(2)



def run_exercise_5():
    print("\nUsing comercio_interno.csv (domestic trade data since the 1990s)")
    print("write a program that:")
    print("\n1) Displays DataFrame dimensions, total entries, column and")
    print("   row names, data types, and the first and last 10 rows.")
    print("\n2) Displays a plot of employment by province ")
    print("   and its relation to the “valor” column.")
    print("\n3) Displays the column alcance_nombre sorted alphabetically.")
    print("\n4) Displays a plot of actividad_producto_nombre grouped by valor.")
    print("\n5) Sums “valor” by alcance_nombre for the years 2009–2019.")
    print("\n6) Displays a plot of actividad_producto_nombre in Mendoza for 2015–2019.\n")

    base_path = os.path.dirname(__file__)
    file_path_test = os.path.abspath(os.path.join(base_path, "..", "..", "..", "..", "data", "commerce_database.csv"))

    print(f"Searching for the file at: {file_path_test} \n")
    data = pd.read_csv(file_path_test, delimiter=",", encoding='latin1')
    df = pd.DataFrame(data)

    data_printing(df)
    series = return_province_values(df)
    chart_of_values_by_province(series)