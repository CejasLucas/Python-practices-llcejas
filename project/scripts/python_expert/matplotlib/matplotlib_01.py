import matplotlib.pyplot as plt
from scripts.utils.terminal_format import TerminalFormat

PIB_2020 = {
    'Brazil': (2364409.9, '#FFB6C1'),    # Rosado claro
    'Mexico': (1309880.9, '#DA70D6'),    # Violeta
    'Argentina': (440769.2, '#87CEFA'),  # Azul claro
    'Colombia': (394571.1, '#00CED1'),   # Cian
    'Chile': (286013.8, '#FF69B4'),      # Rosa fuerte
    'Peru': (210881.6, '#BA55D3'),       # Violeta medio
    'Uruguay': (120532.1, '#ADD8E6'),    # Azul pastel
    'Venezuela': (116067.8, '#40E0D0'),  # Turquesa
    'Ecuador': (88554.7, '#FF1493'),     # Rosado intenso
    'Paraguay': (37260.6, '#8A2BE2'),    # Violeta oscuro
    'Bolivia': (29702.8, '#87CEEB'),     # Azul celeste
    'Guyana': (11780.6, '#00FFFF'),      # Cian brillante
    'Suriname': (11678.2, '#4169E1'),    # Azul royal
}

def run():
    print("Create lists with the GDP data of Latin American countries (2019),")
    print("and generate a bar chart that clearly visualizes the information.\n")
    title = (TerminalFormat.align_left("Country", 20) +
             TerminalFormat.align_right("GDP (millions USD)", 10))

    TerminalFormat.line_with_jump("=", 40)
    print(title)
    TerminalFormat.line("=", 40)
    for country, (gdp, color) in PIB_2020.items():
        print(f"{country:<15} {gdp:>15,.1f}")
    TerminalFormat.line("=", 40)

    country_names = list(PIB_2020.keys())
    country_values = [value for value, color in PIB_2020.values()]
    palette = [color for value, color in PIB_2020.values()]

    plt.figure(figsize=(16, 9), constrained_layout=True)
    bars = plt.bar(country_names, country_values, color=palette)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height,
                 f'{height:,.0f}', ha='center', va='bottom',
                 fontsize=8, rotation=0)

    # Labels
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('GDP (Million USD)', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    plt.gcf().canvas.manager.set_window_title("Matplotlib - Exercise 1")
    plt.suptitle("Latin American Countries in 2020", fontsize=12, fontweight='bold')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()