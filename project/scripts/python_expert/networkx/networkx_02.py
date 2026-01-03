import networkx as nx
from scripts.utils.terminal_format import TerminalFormat
from scripts.utils.graph_styles import THEME_PALETTE, GraphStyle, build_graph

elements = ["Radius", "Diameter", "Eccentricity", "Center", "Periphery", "Density"]

def get_graph_data():
    return [
        ("a", "b", 6), ("a", "c", 9), ("a", "d", 3), ("b", "c", 10),
        ("b", "e", 12), ("c", "d", 4), ("c", "e", 3), ("c", "f", 2),
        ("d", "g", 10), ("d", "f", 15), ("e", "f", 8), ("e", "h", 4),
        ("f", "g", 9), ("f", "i", 10), ("g", "j", 13), ("h", "i", 7),
        ("h", "k", 20), ("i", "j", 15), ("i", "l", 11), ("j", "m", 9),
        ("k", "l", 13), ("k", "n", 6), ("l", "m", 5), ("l", "n", 12), ("m", "n", 5)
    ]


def display_graph_info(mst):
    TerminalFormat().title("GRAPH PROPERTIES (on MST)", "=", 40)
    print(f"Radius: {nx.radius(mst)}")
    print(f"Center: {nx.center(mst)}")
    print(f"Density: {nx.density(mst):.4f}")
    print(f"Diameter: {nx.diameter(mst)}")
    print(f"Periphery: {nx.periphery(mst)}")
    TerminalFormat.line("-", 40)

    TerminalFormat().title("⤵️  Eccentricity per node:", "=", 40)
    for node, ecc in nx.eccentricity(mst).items(): print(f">> Node {node}: {ecc}")
    TerminalFormat.line("-", 40)

    TerminalFormat().title("MINIMUM SPANNING TREE", "~", 40)
    for u, v, w in mst.edges(data='weight'):
        print(f"{u} - {v} (Cost: {w} thousand $)")
    TerminalFormat.line("-", 40)


def run():
    print("\nThe map shows connection points and possible")
    print("telephone lines with costs (in thousands of dollars).")
    print("Find the minimum-cost network that connects all points.")
    print("Draw the graph and calculate:")
    for element in elements: print("-", element)
    info = [(u.upper(), v.upper(), w) for u, v, w in get_graph_data()]

    graph = build_graph(info)
    style_graph = GraphStyle()
    style_graph.draw_graph_pyvis(graph, "Exercise2 Original Telephone Graph")

    mst = nx.minimum_spanning_tree(graph)
    style_graph_mst = GraphStyle(node_color=THEME_PALETTE[3]["node"], edge_color=THEME_PALETTE[3]["edge"])
    style_graph_mst.draw_graph_pyvis(mst, "Exercise2 Minimum Spanning Tree Graph")

    display_graph_info(mst)