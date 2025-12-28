from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

students = {
    'laptop': 80,
    'cellular': 110,
    'ipod': 125,
    'laptop_and_cellular': 62,
    'laptop_and_ipod': 58,
    'cellular_and_ipod': 98,
    'has_all_three': 50
}


def only_has_laptop_and_cellular(): return students['laptop_and_cellular'] - students['has_all_three']
def only_has_laptop_and_ipod(): return students['laptop_and_ipod'] - students['has_all_three']
def only_has_cellular_and_ipod(): return students['cellular_and_ipod'] - students['has_all_three']
def only_has_all_three(): return students['has_all_three']

def only_has_a_laptop():
    return students['laptop'] - only_has_laptop_and_cellular() - only_has_laptop_and_ipod() - only_has_all_three()

def only_has_a_cellular():
    return students['cellular'] - only_has_laptop_and_cellular() - only_has_cellular_and_ipod() - only_has_all_three()

def only_has_a_ipod():
    return students['ipod'] - only_has_laptop_and_ipod() - only_has_cellular_and_ipod() - only_has_all_three()


def data():
    return  {
        '100': only_has_a_laptop(),
        '010': only_has_a_cellular(),
        '001': only_has_a_ipod(),
        '110': only_has_laptop_and_cellular(),
        '101': only_has_laptop_and_ipod(),
        '011': only_has_cellular_and_ipod(),
        '111': only_has_all_three()
    }


def run_exercise_5():
    palette = venn3_colors
    plt.figure(figsize=(8, 6))

    # Call the data() function to get the dictionary with region values
    data_dict = data()

    # Prepare subsets for the Venn diagram
    subsets = {k: v for k, v in data_dict.items()}

    # Create the Venn diagram
    venn = venn3(subsets=subsets, set_labels=('LAPTOP', 'CELLULAR', 'IPOD'), alpha=0.7)

    # Set custom colors for each region using the palette
    for region, count in data_dict.items():
        patch = venn.get_patch_by_id(region)
        if patch:
            patch.set_color(palette[region])
            patch.set_alpha(0.8)

    # Set font size for default subset labels
    for text in venn.subset_labels:
        if text:
            text.set_fontsize(12)

    # Replace default labels with count values
    for region, count in data_dict.items():
        label_obj = venn.get_label_by_id(region)
        if label_obj:
            label_obj.set_text(f"{count}")
            label_obj.set_fontsize(11)

    # Layout and title settings
    plt.tight_layout(pad=2)
    plt.gcf().canvas.manager.set_window_title("Exercise 5")
    plt.suptitle("Venn Diagram: Tech Ownership among Students", fontsize=12, fontweight='bold')
    plt.show()