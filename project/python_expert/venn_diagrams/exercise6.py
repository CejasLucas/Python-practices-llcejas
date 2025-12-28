from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

def set_of_numbers():
    return {
        'A': {100, 110, 120, 140, 150},
        'B': {100, 110, 120, 130, 160},
        'C': {100, 120, 130, 140, 170}
    }

def data():
    A = set_of_numbers()['A']
    B = set_of_numbers()['B']
    C = set_of_numbers()['C']

    return {
        '100': A - B - C,         # Only in A
        '010': B - A - C,         # Only in B
        '001': C - A - B,         # Only in C
        '110': A & B - C,         # A ∩ B, excluding C
        '101': A & C - B,         # A ∩ C, excluding B
        '011': B & C - A,         # B ∩ C, excluding A
        '111': A & B & C          # A ∩ B ∩ C
    }

def run_exercise_6():
    palette = venn3_colors
    plt.figure(figsize=(8, 6))

    data_dict = data()

    # Pass subset sizes (integers) to venn3, not sets
    subsets = {k: len(v) for k, v in data_dict.items()}

    # Create the Venn diagram
    venn = venn3(subsets=subsets, set_labels=('A', 'B', 'C'), alpha=0.7)

    # Apply custom colors to each region
    for region in data_dict:
        patch = venn.get_patch_by_id(region)
        if patch:
            patch.set_color(palette.get(region, '#cccccc'))  # fallback color if not found
            patch.set_alpha(0.8)

    # Display actual set elements (as strings) in each region's label
    for region, values in data_dict.items():
        label_obj = venn.get_label_by_id(region)
        if label_obj:
            if values:
                text = "{" + ", ".join(str(v) for v in sorted(values)) + "}"
            else:
                text = ""  # Empty label if no elements in region
            label_obj.set_text(text)
            label_obj.set_fontsize(10)

    # Final layout and title
    plt.tight_layout(pad=2)
    plt.gcf().canvas.manager.set_window_title("Exercise 6")
    plt.suptitle("Venn Diagram: Elements by Region", fontsize=12, fontweight='bold')
    plt.show()