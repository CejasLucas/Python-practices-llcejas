import networkx as nx
from src.main.Practices.utils_networkx.style_graph import GraphStyle, build_graph, theme_palette

# Mapping node letters to real landmarks in Prague
landmark_names = {
    "A": "Prague Castle",
    "B": "Charles Bridge",
    "C": "Astronomical Clock",
    "D": "Old Town Square",
    "E": "St. Vitus Cathedral",
    "F": "Jewish Quarter",
    "G": "National Museum",
    "H": "Powder Tower",
    "I": "Strahov Monastery"
}

def get_initial_graph_data():
    return [
        ("A", "B", 12), ("A", "D", 6), ("A", "F", 5), ("A", "H", 4),
        ("B", "A", 12), ("B", "C", 7), ("B", "G", 8), ("B", "I", 2),
        ("C", "B", 7), ("C", "D", 7), ("C", "H", 5),
        ("D", "A", 6), ("D", "C", 7), ("D", "E", 2), ("D", "I", 1),
        ("E", "D", 2), ("E", "F", 3), ("E", "G", 3), ("E", "I", 6),
        ("F", "A", 5), ("F", "E", 3), ("F", "G", 6), ("F", "H", 15),
        ("G", "B", 8), ("G", "E", 3), ("G", "F", 6), ("G", "I", 5),
        ("H", "A", 4), ("H", "C", 5), ("H", "F", 15), ("H", "I", 5),
        ("I", "B", 2), ("I", "D", 1), ("I", "E", 6), ("I", "F", 5),
        ("I", "G", 5), ("I", "H", 5)
    ]

def rename_nodes(graph: nx.Graph, mapping: dict):
    """Rename graph nodes using the given mapping."""
    return nx.relabel_nodes(graph, mapping)

def run_exercise_5():
    # Step 1: Build the initial graph
    print("\nAna and Pedro want to visit Prague. The main tourist spots, routes")
    print("and distances (km) are given in a table. Draw the associated graph:")
    for key, landmark in landmark_names.items(): print(f"{key} -> {landmark}")
    graph = build_graph(get_initial_graph_data())

    print("\n" + "=" * 30)
    print(f"{'MAIN GRAPH':^30}")
    print("=" * 30)
    for edge in graph.edges(): print("-", edge)
    print("=" * 30)

    # Step 2: Rename nodes to real Prague landmarks
    graph = rename_nodes(graph, landmark_names)

    # Step 3: Visualize the graph
    style = GraphStyle(node_color=theme_palette[2]["node"], edge_color=theme_palette[2]["edge"])
    style.draw_graph_pyvis(graph, "Exercise5 Prague Tourist Map")

    # Step 4: (Optional) Print shortest paths from Prague Castle
    source = "Prague Castle"
    print(f"\nShortest paths from {source}:\n")
    distances = nx.single_source_dijkstra_path_length(graph, source=source)

    for destination in sorted(distances, key=distances.get):
        print(f"{source} → {destination}: {distances[destination]} km")
    print("End \n")
