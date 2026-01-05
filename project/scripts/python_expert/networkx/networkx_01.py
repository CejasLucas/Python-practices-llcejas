import networkx as nx
from project.scripts.utils.terminal_format import TerminalFormat
from project.scripts.utils.graph_styles import THEME_PALETTE, GraphStyle, build_graph

def get_graph_data():
    return [
        ("Z", "E", 3), ("Z", "F", 2),
        ("Z", "C", 1), ("F", "E", 1),
        ("F", "C", 1), ("E", "D", 2),
        ("C", "B", 5), ("D", "G", 1),
        ("B", "G", 1), ("B", "A", 4),
        ("G", "A", 2), ("D", "A", 5)
    ]

def draw_graph(graph):
    style = GraphStyle(node_color=THEME_PALETTE[2]["node"], edge_color=THEME_PALETTE[2]["edge"])
    style.draw_graph_pyvis(graph, "Exercise1 Dijkstra Graph")

def display_graph_info(graph):
    TerminalFormat().title(f"⤵️  Number of NODES: {graph.number_of_nodes()}", "=", 40)
    print(graph.nodes())
    TerminalFormat.line("-",40)

    TerminalFormat().title(f"⤵️  Number of NODES: {graph.number_of_edges()}", "=", 30)
    for i, edge in enumerate(graph.edges(), start=1):
        if i % 2 == 0:
            print(edge)
        else:
            print(edge, end=' ')
    TerminalFormat.line("-",30)

    shortest_path = nx.dijkstra_path(graph, "Z", "A")
    path_length = nx.dijkstra_path_length(graph, "Z", "A")

    TerminalFormat.line_with_jump("*", 60)
    print("⏹️  Shortest path from Z to A:", shortest_path)
    print("⏹️  Shortest path length:", path_length)
    TerminalFormat.line("*", 60)

    adj_matrix = nx.adjacency_matrix(graph)
    print("\nAdjacency Matrix:")
    print(adj_matrix.todense())
    print()

    inc_matrix = nx.incidence_matrix(graph)
    print("Incidence Matrix:")
    print(inc_matrix.todense())
    print()

def run():
    print("\nUse Dijkstra’s algorithm to find the shortest path between")
    print("vertices Z and A in the given weighted graph. Draw the graph.")
    graph = build_graph(get_graph_data())
    draw_graph(graph)
    display_graph_info(graph)
