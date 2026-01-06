import matplotlib.pyplot as plt
from project.scripts.utils.terminal_format import TerminalFormat

# Data
group_one = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
group_two = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def run():
    print("Plot a scatter chart showing the scores of two groups of athletes")
    print("over a range (x-axis). Use different colors to distinguish the groups.\n")
    title = (TerminalFormat.align_left("Range", 15) +
             TerminalFormat.align_right("First Group", 10) +
             TerminalFormat.align_center("Second Group", 25))

    TerminalFormat.line_with_jump("=", 50)
    print(title)
    TerminalFormat.line("=", 50)
    for i in range(len(grades)):
        print(f"{grades[i]:<10} {group_one[i]:>10,.1f} {group_two[i]:>20,.1f} ")
    TerminalFormat.line("=", 50)

    plt.figure(figsize=(10, 6))
    plt.scatter(grades, group_one, color='blue', label='Group 1', s=100, alpha=0.7)
    plt.scatter(grades, group_two, color='pink', label='Group 2', s=100, alpha=0.7)

    plt.xlabel('Range', fontsize=12)
    plt.ylabel('Qualification', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()

    plt.gcf().canvas.manager.set_window_title("Matplotlib - Exercise 6")
    plt.suptitle("Elements.", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()