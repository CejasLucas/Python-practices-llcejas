from project.utils.__terminal_format__ import TerminalFormat
import matplotlib.pyplot as plt
import numpy as np

country_with_population_area_color = {
    "United States": (331002651, 998193),
    "Brazil": (212559417, 8514877),
    "Mexico": (128932753, 1964375),
    "Colombia": (50882891, 1141748),
    "Argentina": (45195774, 2792600),
    "Canada": (37742154, 9984670),
    "Peru": (33050325, 1285216),
    "Venezuela": (28435940, 916445),
    "Chile": (19116201, 755934),
    "Ecuador": (17643054, 283561),
    "Bolivia": (11673021, 1098585),
    "Cuba": (11326616, 110860),
    "Paraguay": (7132538, 406750),
    "Uruguay": (3473730, 176215)
}

def get_country_names():
    return list(country_with_population_area_color.keys())

def get_population_numbers():
    return [value[0] for value in country_with_population_area_color.values()]

def get_surface_areas():
    return [value[1] for value in country_with_population_area_color.values()]


def run():
    print("Using the provided population and land area data generate")
    print("a graph showing the relationship between population")
    print("and surface area of American and Caribbean countries.")
    title =  (TerminalFormat.align_left("Country", 15) +
              TerminalFormat.align_right("Population", 20) +
              TerminalFormat.align_center("Area", 35 ))

    TerminalFormat.line_with_jump("=", 65)
    print(title)
    TerminalFormat.line("=", 65)
    for country, (population, area) in country_with_population_area_color.items():
        print(f"{country:<15} {population:>20,.1f} {area:>20,.1f}")
    TerminalFormat.line("=", 65)

    countries = get_country_names()
    surfaces = get_surface_areas()
    populations = get_population_numbers()

    fig, ax1 = plt.subplots(figsize=(18, 8))
    x = np.arange(len(countries))
    ax2 = ax1.twinx()
    width = 0.4

    # Fixed colors for all populations and surfaces
    population_color = "#4169E1"
    surface_color = "#FF69B4"

    pop_bars = ax1.bar(x - width/2, populations, width, label='Population', color=population_color, alpha=0.8)
    area_bars = ax2.bar(x + width/2, surfaces, width, label='Surface Area (km²)', color=surface_color, alpha=0.6)

    # Labels and title
    ax1.set_ylabel('Population', color=population_color, fontsize=13, weight='bold')
    ax2.set_ylabel('Surface Area (km²)', color=surface_color, fontsize=13, weight='bold')

    # X-axis labels
    ax1.set_xticks(x)
    ax1.set_xticklabels(countries, rotation=20, fontsize=11)

    # Tick colors matching bar colors
    ax1.tick_params(axis='y', labelcolor=population_color)
    ax2.tick_params(axis='y', labelcolor=surface_color)

    # Combined legend
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    fig.legend(handles1 + handles2, labels1 + labels2, loc="upper right", bbox_to_anchor=(0.9, 0.9), fontsize=13)

    # Window title and layout
    plt.gcf().canvas.manager.set_window_title("Matplotlib - Exercise 3")
    plt.suptitle("Comparison of Population and Surface", fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.show()