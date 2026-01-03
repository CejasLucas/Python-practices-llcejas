import networkx as nx
from project.utils.__terminal_format__ import TerminalFormat
from project.utils.__style_graphic__ import GraphStyle, theme_palette, build_graph

def get_graph_data():
    return [
        ("A", "B", 4),
        ("A", "E", 8),
        ("E", "F", 6),
        ("F", "D", 8),
        ("B", "C", 5),
        ("F", "G", 9),
        ("C", "G", 8),
        ("G", "H", 11),
        ("F", "H", 11)
    ]

def display_graph_info(graph: nx.Graph, path: list[str], cost: float):
    TerminalFormat().title(f"⤵️  Number of NODES: {graph.number_of_nodes()}", "=", 40)
    print(graph.nodes())
    TerminalFormat.line("-", 40)

    TerminalFormat().title(f"⤵️  Number of NODES: {graph.number_of_edges()}", "=", 40)
    for i, edge in enumerate(graph.edges(), start=1):
        if i % 3 == 0:
            print(edge)
        else:
            print(edge, end=' ')
    TerminalFormat.line("-", 40)

    TerminalFormat.line_with_jump("~", 40)
    print(f">> Total fuel needed: {cost} units")
    print("Shorted Path: " + " ➡️  ".join(path))
    TerminalFormat.line("~", 40)


def highlight_path_subgraph(graph: nx.Graph, path: list[str]) -> nx.Graph:
    edges_in_path = [(path[i], path[i+1]) for i in range(len(path) - 1)]
    path_subgraph = nx.Graph()
    for u, v in edges_in_path:
        weight = graph[u][v]["weight"]
        path_subgraph.add_edge(u, v, weight=weight)
    return path_subgraph

def run():
    print("\nGiven a weighted graph G = (V, A) with vertices A–H")
    print("representing towns and edge weights as fuel usage,")
    print("determine the fuel needed for the shortest route from A to H.")
    graph = build_graph(get_graph_data())
    base_style = GraphStyle()
    base_style.draw_graph_pyvis(graph, "Exercise3 Transportation Map")

    source, target = "A", "H"
    shortest_path = nx.dijkstra_path(graph, source=source, target=target)
    total_cost = nx.dijkstra_path_length(graph, source=source, target=target)

    path_subgraph = highlight_path_subgraph(graph, shortest_path)
    highlight_style = GraphStyle(node_color=theme_palette[2]["node"], edge_color=theme_palette[2]["edge"])
    highlight_style.draw_graph_pyvis(path_subgraph, "Exercise3 Shortest path")

    display_graph_info(graph, shortest_path, total_cost)
