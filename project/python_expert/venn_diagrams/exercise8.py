from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors
from matplotlib import pyplot as plt
from matplotlib_venn import venn3
from matplotlib import patheffects
from colorama import Fore, Style

def transport_media_survey():
    return {
        '100': ('Only Subway', 1150),     # only subway
        '010': ('Only Motorbike', 400),   # only motorbike
        '001': ('Only Collective', 700),  # only collective
        '110': ('Subway & Motorbike', 0),
        '101': ('Subway & Collective', 800),
        '011': ('Motorbike & Collective', 0),
        '111': ('All Three', 0)
    }

def run_exercise_8():
    data = transport_media_survey()

    # Extract values for logic
    only_subway = data['100'][1]
    only_motorbike = data['010'][1]
    only_collective = data['001'][1]
    subway_and_motorbike = data['110'][1]
    subway_and_collective = data['101'][1]
    motorbike_and_collective = data['011'][1]
    all_three = data['111'][1]

    total_surveyed = 3200
    total_users = sum([count for _, count in data.values()])
    no_transport = total_surveyed - total_users

    # a. People who only use subway
    result_a = only_subway

    # b. People who use at most two transport methods
    only_one_transport = only_subway + only_motorbike + only_collective
    exactly_two_transports = subway_and_collective
    result_b = only_one_transport + exactly_two_transports

    # Print results
    print(">> Exercise 8 - Transport Survey Summary")
    print(f"a. People who only use subway: {result_a}")
    print(f"b. People who use at most two transport methods: {result_b}")
    print(f"c. People who use no transport methods: {no_transport}")

    # Create Venn Diagram
    subset_dict = {
        '100': float(only_subway),
        '010': float(only_motorbike),
        '001': float(only_collective),
        '110': float(subway_and_motorbike),
        '101': float(subway_and_collective),
        '011': float(motorbike_and_collective),
        '111': float(all_three)
    }

    region_keys = ['100', '010', '001', '110', '101', '011', '111']
    palette = venn3_colors

    venn = venn3(subsets=subset_dict, set_labels=("Subway", "Motorbike", "Collective"))

    for key in region_keys:
        patch = venn.get_patch_by_id(key)
        if patch and key in palette:
            patch.set_color(palette[key])
            patch.set_alpha(0.8)

    for key in region_keys:
        label = venn.get_label_by_id(key)
        if label:
            label.set_text(str(int(subset_dict[key])))
            label.set_fontsize(10)
            label.set_color('white')
            label.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black')])

    # Texto adicional
    plt.text(0.75, -0.55,
             f"No transport: {no_transport}",
             horizontalalignment='center',
             fontsize=10,
             bbox=dict(boxstyle="round", ec="gray", fc="white"))

    plt.tight_layout(pad=2)
    plt.gcf().canvas.manager.set_window_title("Exercise 8")
    plt.suptitle("Venn Diagram: Transport Media Survey", fontsize=12, fontweight='bold')
    plt.show()

    # Consistency check
    if total_users + no_transport == total_surveyed:
        print(Fore.GREEN + "\nData is consistent.\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Inconsistency detected in the data.\n" + Style.RESET_ALL)