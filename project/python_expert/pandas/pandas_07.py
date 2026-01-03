import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from project.utils.__location__ import data_file

DATA_FILE = data_file("salaries_database.csv")
custom_colors = ['#6C63FF', '#F5B7B1', '#FF6584']

# Helper function to print a visual delimiter
def number_of_spaces(number): return print('\n' * number)

def title_center_text(text, number): return print(f"{f'{text}':^{number}}")

def space_with_delimiter(number, delimiter): print(delimiter * number)


def print_seniority_stats(df):
    df['yrs.service'] = pd.to_numeric(df['yrs.service'], errors='coerce')
    min_years = df['yrs.service'].min()
    max_years = df['yrs.service'].max()
    mean_years = df['yrs.service'].mean()

    number_of_spaces(1)
    space_with_delimiter(70,"=")
    title_center_text("Seniority Statistics (Years of Service)", 50)
    space_with_delimiter(70, "=")
    print(f"- Minimum: {min_years:.2f} years")
    print(f"- Maximum: {max_years:.2f} years")
    print(f"- Average: {mean_years:.2f} years")
    space_with_delimiter(70,"-")
    number_of_spaces(1)


def plot_rank_pie_chart(df):
    rank_counts = df['rank'].value_counts()
    labels = rank_counts.index
    sizes = rank_counts.values

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=custom_colors[:len(labels)],
        textprops={'fontsize': 10, 'fontweight': 'bold'}
    )
    plt.title("Percentage of Professors by Rank", fontsize=16)
    plt.gcf().canvas.manager.set_window_title("Exercise 7")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def aggregate_salary_stats(df):
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df['rank'] = df['rank'].astype(str)

    aggregation = df.groupby('rank')['salary'].agg([
        ('Sum', np.sum),
        ('Mean', np.mean),
        ('Standard Deviation', np.std)
    ]).sort_values(by='Sum', ascending=False)

    space_with_delimiter(70, "=")
    title_center_text("Aggregated Salary Statistics by Rank", 70)
    space_with_delimiter(70, "=")
    print(aggregation)
    space_with_delimiter(70, "-")
    return aggregation

def run():
    print("\nThe salaries file shows categories, seniority, salaries, etc.")
    print("a. Calculate the min, max, and average of seniority.")
    print("b. Write code to create a chart showing the percentage of each position.")
    print("c. Write code to group and aggregate data to compute sum, mean, ")
    print("   and standard deviation of salary using NumPy functions (np.sum).\n")

    print(f"Loading salary data from: {DATA_FILE}")
    df = pd.read_csv(DATA_FILE, delimiter=",", encoding="latin1")

    print_seniority_stats(df)
    plot_rank_pie_chart(df)
    aggregate_salary_stats(df)