from src.main.Practices.utils_venn_diagrams.palette_colors import venn2_colors
from matplotlib import pyplot as plt
from matplotlib import patheffects
from matplotlib_venn import venn2
from colorama import Fore, Style

# Venn2 Diagram
x_base = 0.75
y_base = -0.55
spacing = 0.09

# Number of students in each category
enrolled_students = 500
enrolled_in_algebra = 125
enrolled_in_sports = 275
enrolled_in_sports_and_algebra = 52

# Prepare Venn diagram data
data = {
    '10': ('Only Sports', enrolled_in_sports - enrolled_in_sports_and_algebra),
    '01': ('Only Algebra', enrolled_in_algebra - enrolled_in_sports_and_algebra),
    '11': ('Algebra and Sports', enrolled_in_sports_and_algebra)
}

def run_exercise_3():
    # Get color palette
    palette = venn2_colors

    # Calculate totals
    total_from_sets = sum([v[1] for v in data.values()])
    outside_venn = enrolled_students - total_from_sets

    # Create the Venn diagram
    venn = venn2(
        subsets=(data['10'][1], data['01'][1], data['11'][1]),
        set_labels=(data['10'][0], data['01'][0])
    )

    # Apply colors to each subset region
    for key in ['10', '01', '11']:
        patch = venn.get_patch_by_id(key)
        if patch:
            patch.set_color(palette[key])
            patch.set_alpha(0.8)

    # Add text labels with outline effect
    for key in ['10', '01', '11']:
        label = venn.get_label_by_id(key)
        if label:
            label.set_text(str(data[key][1]))
            label.set_fontsize(10)
            label.set_color('white')
            label.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black')])

    # Add explanatory text below the diagram
    for i, key in enumerate(['10', '01', '11']):
        label, count = data[key]
        plt.text(
            x_base, y_base - i * spacing,
            f"{label}: {count} students",
            size=9,
            ha="center",
            bbox=dict(boxstyle="round", ec="gray", fc="white")
        )

    # Display number of students outside both sets
    plt.text(
        x_base, y_base - 3 * spacing,
        f"Outside both Algebra and Sports: {outside_venn} students",
        size=9,
        ha="center",
        bbox=dict(boxstyle="round", ec="gray", fc="white")
    )

    # Show the final diagram
    plt.gcf().canvas.manager.set_window_title("Exercise 3")
    plt.suptitle("Venn Diagram: Enrollment distribution", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()

    # Print summary to the console
    print(">> Venn2 - Enrollment Summary")
    for key in ['10', '01', '11']:
        label, count = data[key]
        print(f"{label:<25}: {count}")
    print(f"{'-' * 30}")
    print(f"{'Total students':<25}: {enrolled_students}")
    print(f"{'Counted in Venn':<25}: {total_from_sets}")
    print(f"{'Outside both sets':<25}: {outside_venn}")

    # Validate data consistency
    if total_from_sets + outside_venn == enrolled_students:
        print(Fore.GREEN + "\nData is consistent.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED +"Inconsistency detected in the data.\n" + Style.RESET_ALL)
