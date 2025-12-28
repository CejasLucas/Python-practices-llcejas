from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
from matplotlib import patheffects
from colorama import Fore, Style

# Survey data adapted from the "language" example to a pet owners context
def pet_owners_survey():
    return {
        '100': ('Only Dogs', 30),
        '010': ('Only Cats', 42),
        '001': ('Only Others', 21),
        '110': ('Dogs & Cats', 20),
        '101': ('Dogs & Others', 8),
        '011': ('Cats & Others', 10),
        '111': ('All Three', 5)
    }

def run_exercise_7():
    data = pet_owners_survey()

    # Extract counts for calculations
    only_dog = data['100'][1]
    only_cat = data['010'][1]
    only_other = data['001'][1]
    dog_and_cat = data['110'][1]
    dog_and_other = data['101'][1]
    cat_and_other = data['011'][1]
    all_three = data['111'][1]

    total_with_pets = sum([count for _, count in data.values()])
    total_surveyed = 150
    no_pets = total_surveyed - total_with_pets

    # Prepare subsets dict (order and keys important for venn3)
    region_keys = ['100', '010', '001', '110', '101', '011', '111']
    subset_dict = {k: float(data[k][1]) for k in region_keys}
    palette = venn3_colors

    # Create Venn3 diagram
    venn = venn3(subsets=subset_dict, set_labels=(data['100'][0], data['010'][0], data['001'][0]))

    # Color each subset region using palette
    for key in region_keys:
        patch = venn.get_patch_by_id(key)
        if patch and key in palette:
            patch.set_color(palette[key])
            patch.set_alpha(0.8)

    # Add labels with outline effect for better readability
    for key in region_keys:
        label = venn.get_label_by_id(key)
        if label:
            label.set_text(str(int(subset_dict[key])))
            label.set_fontsize(10)
            label.set_color('white')
            label.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black')])

    # Add no pets text below diagram
    plt.text(0.75, -0.75,
             f"No pets at all: {no_pets}",
             horizontalalignment='center',
             fontsize=10,
             bbox=dict(boxstyle="round", ec="gray", fc="white"))

    plt.tight_layout(pad=2)
    plt.gcf().canvas.manager.set_window_title("Exercise 7")
    plt.suptitle("Venn Diagram: Pet Owners Survey", fontsize=12, fontweight='bold')
    plt.show()

    # Print summary to console
    print(">> Exercise 7 - Pet Owners Summary")
    print(f"1. How many had dogs and cats but no other pets? Response: {dog_and_cat}")
    print(f"2. How many only had dogs? Response: {only_dog}")
    print(f"3. How many had no pets at all? Response: {no_pets}")
    print(f"4. How many other pet owners also had dogs or cats, but not both? Response: {dog_and_other + cat_and_other}")

    # Basic data consistency check
    if total_with_pets + no_pets == total_surveyed:
        print(Fore.GREEN + "\nData is consistent.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Inconsistency detected in the data.\n" + Style.RESET_ALL)