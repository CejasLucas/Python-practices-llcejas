from project.scripts.python_expert.networkx import (
    networkx_01,
    networkx_02,
    networkx_03,
    networkx_04,
    networkx_05,
    networkx_06
)

def get_statements_with_networkx_exercises():
    return [
        {"statement": "Dijkstra shortest path (Z to A)", "exercise": networkx_01},
        {"statement": "Minimal telephone network & analysis", "exercise": networkx_02},
        {"statement": "Fuel optimization between cities (A to H)", "exercise": networkx_03},
        {"statement": "Distance analysis between cities", "exercise": networkx_04},
        {"statement": "Trip to Prague: routes & landmarks", "exercise": networkx_05},
        {"statement": "Employee computer network analysis", "exercise": networkx_06}
    ]
