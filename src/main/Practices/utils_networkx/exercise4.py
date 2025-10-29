import networkx as nx
from src.main.Practices.utils_networkx.style_graph import GraphStyle, build_graph, theme_palette

source = "A"
target = "H"
intermediate1 = "B"
intermediate2 = "G"
desired_total_distance = 68

def get_initial_graph_data():
    return [
        ("A", "B", 20), ("A", "F", 34), ("A", "I", 45), ("B", "C", 20), ("B", "F", 10),
        ("B", "I", 26), ("C", "D", 28), ("C", "I", 22), ("D", "G", 18), ("D", "H", 19),
        ("D", "I", 13), ("E", "F", 22), ("E", "G", 12), ("E", "H", 25), ("F", "G", 30),
        ("F", "I", 12), ("G", "H", 16), ("G", "I", 14), ("H", "I", 32)
    ]

def compute_required_bg_weight(graph: nx.Graph):
    ab = graph.get_edge_data(source, intermediate1, {}).get("weight")
    gh = graph.get_edge_data(intermediate2, target, {}).get("weight")
    if ab is None or gh is None:
        raise ValueError("One of the edges required to calculate the required weight is missing.")
    return desired_total_distance - ab - gh


def print_shortest_paths(graph: nx.Graph):
    print(f"\nShortest distances from {source}:")
    distances = nx.single_source_dijkstra_path_length(graph, source=source)

    for node in sorted(distances):
        print(f"{source} → {node}: {distances[node]} km")
    print(f"\nShortest path from {source} to {target}:")

    path = nx.dijkstra_path(graph, source, target)
    cost = nx.dijkstra_path_length(graph, source, target)
    print(" → ".join(path))
    print(f"Total distance: {cost} km")


def run_exercise_4():
    print("\nFor the weighted graph G where vertices")
    print("are cities and weights are distances (km):")
    print(" a) Using the appropriate algorithm, find the")
    print(" shortest distances from A to all other cities.")
    print(" b) A new route between B and G changes the distance")
    print(" from A to H to 68 km. Find the weight of edge {B, G}.")

    # Step 1: build the initial graph
    graph = build_graph(get_initial_graph_data())
    print("\n" + "=" * 30)
    print(f"{'MAIN GRAPH':^30}")
    print("=" * 30)
    for edge in graph.edges(): print("-", edge)
    print("=" * 30)

    # Step 2: visualize the original graph
    original_style = GraphStyle(node_color=theme_palette[3]["node"], edge_color=theme_palette[3]["edge"])
    original_style.draw_graph_pyvis(graph, "Exercise4 Original city graph")

    # Step 3: compute and add the new edge (B, G)
    required_weight = compute_required_bg_weight(graph)
    graph.add_edge(intermediate1, intermediate2, weight=required_weight)

    # Step 4: visualize the updated graph
    updated_style = GraphStyle(node_color=theme_palette[2]["node"], edge_color=theme_palette[2]["edge"])
    updated_style.draw_graph_pyvis(graph, "Exercise4 Updated city graph with (B,G)")

    # Step 5: print results
    print_shortest_paths(graph)
    print(f"\nNew edge ({intermediate1}, {intermediate2}) added with weight: {required_weight} km \n")