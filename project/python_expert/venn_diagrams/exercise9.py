from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Survey data: number of families with children in different education levels
education_data = {
    'university': 38,
    'high_school': 72,
    'elementary': 71,
    'university_and_high_school': 16,
    'university_and_elementary': 22,
    'high_school_and_elementary': 30,
    'all_three_levels': 10
}

# Overlapping group calculations
def all_three_levels(): return education_data['all_three_levels']
def university_and_high_school(): return education_data['university_and_high_school'] - all_three_levels()
def university_and_elementary(): return education_data['university_and_elementary'] - all_three_levels()
def high_school_and_elementary(): return education_data['high_school_and_elementary'] - all_three_levels()

# Exclusive group calculations
def only_university():
    return education_data['university'] - university_and_high_school() - university_and_elementary() - all_three_levels()

def only_high_school():
    return education_data['high_school'] - university_and_high_school() - high_school_and_elementary() - all_three_levels()

def only_elementary():
    return education_data['elementary'] - university_and_elementary() - high_school_and_elementary() - all_three_levels()

# Structure the data for the Venn diagram
def venn_data():
    return {
        '100': only_university(),
        '010': only_high_school(),
        '001': only_elementary(),
        '110': university_and_high_school(),
        '101': university_and_elementary(),
        '011': high_school_and_elementary(),
        '111': all_three_levels()
    }

# Main function to run and display the Venn diagram
def run_exercise_9():
    palette = venn3_colors
    plt.figure(figsize=(8, 6))

    data_dict = venn_data()
    subsets = {k: v for k, v in data_dict.items()}

    venn = venn3(subsets=subsets, set_labels=('UNIVERSITY', 'HIGH SCHOOL', 'ELEMENTARY'), alpha=0.7)

    # Set custom colors for each region
    for region, count in data_dict.items():
        patch = venn.get_patch_by_id(region)
        if patch:
            patch.set_color(palette[region])
            patch.set_alpha(0.8)

    # Set font size for subset labels
    for text in venn.subset_labels:
        if text:
            text.set_fontsize(12)

    # Display actual counts in each region
    for region, count in data_dict.items():
        label_obj = venn.get_label_by_id(region)
        if label_obj:
            label_obj.set_text(f"{count}")
            label_obj.set_fontsize(11)

    # Summary: families with no children in any level
    total_families = 150
    families_with_students = sum(data_dict.values())
    families_with_no_students = total_families - families_with_students

    # Add summary textbox
    plt.text(0.75, -0.55,
             f"No students in school: {families_with_no_students}",
             horizontalalignment='center',
             fontsize=10,
             bbox=dict(boxstyle="round", ec="gray", fc="white"))

    # Final layout and title
    plt.tight_layout(pad=2)
    plt.gcf().canvas.manager.set_window_title("Exercise 9")
    plt.suptitle("Venn Diagram: Educational Levels Among Families", fontsize=12, fontweight='bold')
    plt.show()