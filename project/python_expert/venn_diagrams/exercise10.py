from src.main.Practices.utils_venn_diagrams.palette_colors import venn3_colors
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

total = 500

def subjects():
    mathematics = 329
    physics = 186
    chemistry = 295
    mathematics_physics = 83
    mathematics_chemistry = 217
    physics_chemistry = 63

    MPC = total - (mathematics + physics + chemistry) + (mathematics_physics + mathematics_chemistry + physics_chemistry)

    only_MP = mathematics_physics - MPC
    only_MC = mathematics_chemistry - MPC
    only_PC = physics_chemistry - MPC

    only_M = mathematics - (only_MP + only_MC) - MPC
    only_P = physics - (only_MP + only_PC) - MPC
    only_C = chemistry - (only_MC + only_PC) - MPC

    return {
        '100': only_M,
        '010': only_P,
        '001': only_C,
        '110': only_MP,
        '101': only_MC,
        '011': only_PC,
        '111': MPC,
        'total': total
    }

def run_exercise_10():
    data = subjects()
    palette = venn3_colors

    plt.figure(figsize=(8, 6))
    venn = venn3(
        subsets={k: v for k, v in data.items() if k in ['100', '010', '001', '110', '101', '011', '111']},
        set_labels=('MATHEMATICS', 'PHYSICS', 'CHEMISTRY'),
        alpha=0.7
    )

    # Colores personalizados
    for region in ['100', '010', '001', '110', '101', '011', '111']:
        patch = venn.get_patch_by_id(region)
        if patch:
            patch.set_color(palette[region])
            patch.set_alpha(0.8)

    # Etiquetas
    for text in venn.subset_labels:
        if text:
            text.set_fontsize(12)

    for region in ['100', '010', '001', '110', '101', '011', '111']:
        label = venn.get_label_by_id(region)
        if label:
            label.set_text(f"{data[region]}")
            label.set_fontsize(11)

    plt.text(0.75, -0.55,
             f"Total students: {total}",
             horizontalalignment='center',
             fontsize=10,
             bbox=dict(boxstyle="round", ec="gray", fc="white"))

    plt.tight_layout(pad=2)
    plt.gcf().canvas.manager.set_window_title("Exercise 10")
    plt.suptitle("Venn Diagram: Subject Enrollment", fontsize=12, fontweight='bold')
    plt.show()