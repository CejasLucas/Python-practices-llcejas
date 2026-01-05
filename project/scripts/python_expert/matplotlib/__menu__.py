from project.scripts.python_expert.matplotlib.matplotlib_01 import run as ex_01
from project.scripts.python_expert.matplotlib.matplotlib_02 import run as ex_02
from project.scripts.python_expert.matplotlib.matplotlib_03 import run as ex_03
from project.scripts.python_expert.matplotlib.matplotlib_04 import run as ex_04
from project.scripts.python_expert.matplotlib.matplotlib_05 import run as ex_05
from project.scripts.python_expert.matplotlib.matplotlib_06 import run as ex_06

def get_statements_with_matplotlib_exercises():
    return [
        {"statement": "Bar chart of Latin American GDP (2019)", "exercise": ex_01},
        {"statement": "GDP percentage pie chart", "exercise": ex_02},
        {"statement": "Scatter plot: population vs. surface", "exercise": ex_03},
        {"statement": "Grouped bar chart of product outputs", "exercise": ex_04},
        {"statement": "Stacked bar chart: beverage consumption", "exercise": ex_05},
        {"statement": "Scatter plot: athlete group scores", "exercise": ex_06}
    ]
