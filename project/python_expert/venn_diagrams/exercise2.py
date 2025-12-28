from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors
from matplotlib import pyplot as plt
from matplotlib import patheffects
from matplotlib_venn import venn3
from colorama import Fore, Style

x_base = 0.45
y_base = -0.45
spacing = 0.1

# Data binary keys: (label, count)
data = {
    '100': ('French only', 450),
    '010': ('English only', 0),
    '001': ('Spanish only', 100),
    '110': ('French & English', 50),
    '101': ('French & Spanish', 0),
    '011': ('English & Spanish', 0),
    '111': ('All three', 0)
}

def run_exercise_2():
    region_keys = ['100', '010', '001', '110', '101', '011', '111']
    subset_dict = {k: float(data[k][1]) for k in region_keys}
    palette = venn3_colors

    # Create Venn diagram
    venn = venn3(subsets=subset_dict, set_labels=(data['100'][0], data['110'][0], data['001'][0]))

    # Apply custom colors to each region
    for key in region_keys:
        patch = venn.get_patch_by_id(key)
        if patch and key in palette:
            patch.set_color(palette[key])
            patch.set_alpha(1.0)

    # Add count labels to each region
    for key in region_keys:
        count = subset_dict[key]
        label = venn.get_label_by_id(key)
        if label:
            label.set_text(str(int(count)))  # Show as integer
            label.set_fontsize(10)
            label.set_color('white')
            label.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black')])

    # Add descriptive text below the diagram
    for i, key in enumerate(['100', '010', '001']):
        label, count = data[key]
        plt.text(
            x_base, y_base - i * spacing,
            f"{label}: {count} students",
            size=9,
            ha="left",
            bbox=dict(boxstyle="round", ec="gray", fc="lightyellow")
        )

    # Display the diagram
    plt.gcf().canvas.manager.set_window_title("Exercise 2")
    plt.suptitle("Venn Diagram: Distribution of Language", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()

    # Print summary to console
    print("\n>> Venn3 - Language Study Summary")
    total_students = sum(int(count) for _, count in data.values())
    for key in region_keys:
        label, count = data[key]
        print(f"{label:<25}: {count}")
    print(f"{'-' * 30}")
    print(f"{'Total students':<25}: {total_students}")

    # Check data consistency
    if sum(subset_dict.values()) == total_students:
        print(Fore.GREEN + "\nData is consistent.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"\nInconsistency: subset sum = {sum(subset_dict.values())}, expected = {total_students} \n" + Style.RESET_ALL)