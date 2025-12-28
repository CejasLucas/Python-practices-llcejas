from src.main.Practices.utils_venn_diagrams.palette_colors import venn2_colors
from matplotlib import pyplot as plt
from matplotlib import patheffects
from matplotlib_venn import venn2
from colorama import Fore, Style

# Survey data
survey = {
    'argentines': 425,
    'brazilians': 575,
    'number_of_people_surveyed': 900,
    'number_of_people_present': 1000
}

# Number of people who were present but not surveyed
def number_of_people_not_surveyed():
    return survey['number_of_people_present'] - survey['number_of_people_surveyed']

# Number of people who identified as both Argentines and Brazilians (overlap)
def number_of_immigrants():
    return survey['argentines'] + survey['brazilians'] - survey['number_of_people_surveyed']

# Prepare values for the Venn diagram
def values_for_the_diagram():
    intersect = number_of_immigrants()
    only_arg = survey['argentines'] - intersect
    only_bra = survey['brazilians'] - intersect
    return only_arg, only_bra, intersect

def run_exercise_4():
    # Get data values
    palette = venn2_colors
    only_arg, only_bra, both = values_for_the_diagram()

    # Total number of people present
    enrolled_students = survey['number_of_people_present']
    total_from_sets = only_arg + only_bra + both
    outside_venn = enrolled_students - total_from_sets

    # Create the Venn diagram
    venn = venn2(subsets=(only_arg, only_bra, both), set_labels=('Argentines', 'Brazilians'))

    # Apply colors to each region
    for key in ['10', '01', '11']:
        patch = venn.get_patch_by_id(key)
        if patch:
            patch.set_color(palette[key])
            patch.set_alpha(0.8)

    # Add labels inside the diagram with stroke effect
    for key in ['10', '01', '11']:
        label = venn.get_label_by_id(key)
        if label:
            count = {'10': only_arg, '01': only_bra, '11': both}[key]
            label.set_text(str(count))
            label.set_fontsize(10)
            label.set_color('white')
            label.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black')])

    # Base position for annotations
    x_base, y_base, spacing = 0.75, -0.75, 0.095
    descriptions = {
        "10": ("Only Argentines", only_arg),
        "01": ("Only Brazilians", only_bra),
        "11": ("Both Argentines and Brazilians", both)
    }


    # Add annotations below the diagram
    for i, key in enumerate(['10', '01', '11']):
        label, count = descriptions[key]
        plt.text(
            x_base, y_base - i * spacing,
            f"{label}: {count} people",
            size=9.5, ha="center",
            bbox=dict(boxstyle="round", ec="gray", fc="white")
        )

    # Show the diagram
    plt.gcf().canvas.manager.set_window_title("Exercise 4")
    plt.suptitle("Venn Digram: Number of people surveyed", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()

    # Print summary in the console
    print(">> Venn2 - Survey Summary")
    for key in ['10', '01', '11']:
        label, count = descriptions[key]
        print(f"{label:<35}: {count}")
    print(f"{'-' * 40}")
    print(f"{'Total people present':<35}: {enrolled_students}")
    print(f"{'Counted in Venn':<35}: {total_from_sets}")
    print(f"{'Not surveyed':<35}: {outside_venn}")

    # Check for data consistency
    if total_from_sets + outside_venn == enrolled_students:
        print(Fore.GREEN + "\nData is consistent.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Inconsistency detected in the data.\n" + Style.RESET_ALL)