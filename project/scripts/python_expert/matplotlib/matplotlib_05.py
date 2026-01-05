import numpy as np
import matplotlib.pyplot as plt
from project.scripts.utils.terminal_format import TerminalFormat

# Data
names = ['María', 'Pablo', 'Ema', 'Franco', 'Estefanía', 'Pedro']
tea = np.array([1, 2, 5, 2, 1, 3])
water = np.array([10, 3, 14, 12, 15, 13])
coffee = np.array([5, 5, 7, 6, 7, 4])

def run():
    print("Using the drink intake data (coffee, tea, and water) ")
    print("for six people over six days, create a stacked bar chart.")
    print("Determine who drinks the most and who drinks the least.")
    print("Could this data also be represented using a box plot?\n")
    title = f"{'Name':<10} {'Tea':>10} {'Water':>10} {'Coffee':>10}"

    TerminalFormat.line_with_jump("=", 50)
    print(title)
    TerminalFormat.line("=", 50)
    for i in range(len(names)):
        print(f"{names[i]:<10} {tea[i]:>10,.1f} {water[i]:>10,.1f} {coffee[i]:>8,.1f} ")
    TerminalFormat.line("=", 50)

    # Configuration basic
    x = np.arange(len(names))
    width = 0.25

    # Create
    fig, ax = plt.subplots(figsize=(12, 6))

    violet_color = "#6C63FF"
    water_color = "#3B6978"
    cian_color = "#00D1B2"

    ax.bar(x - width, tea, width, label='Tea', color=violet_color)
    ax.bar(x, water, width, label='Water', color=water_color)
    ax.bar(x + width, coffee, width, label='Coffee', color=cian_color)

    # Labels
    ax.set_ylabel('Number of Drinks')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=0)
    ax.legend()

    plt.gcf().canvas.manager.set_window_title("Matplotlib - Exercise 5")
    plt.suptitle("Beverage Consumption by Person.", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()