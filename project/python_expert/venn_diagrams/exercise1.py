import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors

data = {
    '100': (5, 'Motorbike only'),
    '010': (46, 'Car only'),
    '001': (14, 'Bicycle only'),

    '110': (20, 'Motorbike and Car'),
    '101': (3, 'Motorbike and Bicycle'),
    '011': (10, 'Car and Bicycle'),

    '111': (10, 'All Three')
}

def run_exercise_1():
    palette = venn3_colors
    plt.figure(figsize=(8, 6))
    subsets = { k: v[0] for k, v in data.items()}
    # Create Venn diagram
    venn = venn3(subsets=subsets, set_labels=('MOTORBIKE', 'CAR', 'BICYCLE'), alpha=0.7)

    for region, (count, label) in data.items():
        patch = venn.get_patch_by_id(region)
        if patch:
            patch.set_color(palette[region])
            patch.set_alpha(0.8)


    for text in venn.subset_labels:
        if text:
            text.set_fontsize(12)

    for region, (count, label) in data.items():
        label_obj = venn.get_label_by_id(region)
        if label_obj:
            label_obj.set_text(f"{label}\n({count})")
            label_obj.set_fontsize(11)

    plt.tight_layout(pad=2)
    plt.gcf().canvas.manager.set_window_title("Exercise 1")
    plt.suptitle("Venn Diagram: Transportation Preferences", fontsize=12, fontweight='bold')
    return plt.show()