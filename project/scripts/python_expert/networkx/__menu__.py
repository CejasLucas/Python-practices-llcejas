from project.scripts.python_expert.networkx.networkx_01 import run as ex_01
from project.scripts.python_expert.networkx.networkx_02 import run as ex_02
from project.scripts.python_expert.networkx.networkx_03 import run as ex_03
from project.scripts.python_expert.networkx.networkx_04 import run as ex_04
from project.scripts.python_expert.networkx.networkx_05 import run as ex_05
from project.scripts.python_expert.networkx.networkx_06 import run as ex_06

def get_statements_with_networkx_exercises():
    return [
        {"statement": "Dijkstra shortest path (Z to A)", "exercise": ex_01},
        {"statement": "Minimal telephone network & analysis", "exercise": ex_02},
        {"statement": "Fuel optimization between cities (A to H)", "exercise": ex_03},
        {"statement": "Distance analysis between cities", "exercise": ex_04},
        {"statement": "Trip to Prague: routes & landmarks", "exercise": ex_05},
        {"statement": "Employee computer network analysis", "exercise": ex_06}
    ]
