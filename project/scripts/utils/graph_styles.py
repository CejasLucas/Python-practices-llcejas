import webbrowser
import networkx as nx
from pathlib import Path
from pyvis.network import Network

PROJECT_ROOT = Path(__file__).resolve().parents[4]
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)  # Check if the folder exists, create it if not

THEME_PALETTE = {
    1: {"node": "#6C63FF", "edge": "#9D8CFF"},
    2: {"node": "#00D1B2", "edge": "#66E0D6"},
    3: {"node": "#FF7FBF", "edge": "#FFB0D1"},
    4: {"font": "#141414", "label": "#0A0A0A"}
}


class GraphStyle:
    edge_font_size = 10
    node_font_size = 25
    node_size = 30

    def __init__(
            self,
            node_color=THEME_PALETTE[1]["node"],
            node_font_color=THEME_PALETTE[4]["label"],
            edge_color=THEME_PALETTE[1]["edge"],
            edge_label_color=THEME_PALETTE[4]["font"]
    ):
        self.node_color = node_color
        self.node_font_color = node_font_color
        self.edge_color = edge_color
        self.edge_label_color = edge_label_color

    def apply_node_style(self, net, node):
        # Apply styles for each node
        net.add_node(
            node,
            label=node,
            color=self.node_color,
            font={'size': self.node_font_size, 'color': self.node_font_color, 'bold': True},
            size=self.node_size
        )

    def apply_edge_style(self, net, u, v, data_edge):
        # Apply styles for each edge
        weight = data_edge.get('weight', 1)
        net.add_edge(
            u, v,
            value=weight,
            width=weight,
            label=str(weight),
            title=f"Weight: {weight}",
            color=self.edge_color,
            font={'size': self.edge_font_size, 'color': self.edge_label_color}
        )

    def draw_graph_pyvis(self, graph, title):
        # Create and style the graph using pyvis
        net = Network(height="750px", width="100%", directed=False, notebook=False)

        # Apply node and edge styles
        for node in graph.nodes():
            self.apply_node_style(net, node)

        for u, v, data_edge in graph.edges(data=True):
            self.apply_edge_style(net, u, v, data_edge)

        # Add control buttons for physics settings
        net.show_buttons(filter_=['physics'])

        # Apply physics settings for graph layout
        net.barnes_hut(
            spring_length=50,
            spring_strength=0.005,
            gravity=-2000,
            central_gravity=0.3,
            damping=0.09,
            overlap=0.1
        )

        # Ensure the filename is unique
        file_name = f"{title.replace(' ', '_').lower()}.html"
        file_path = OUTPUT_DIR / file_name

        # Check if the HTML file already exists
        if not file_path.exists():
            net.save_graph(str(file_path))  # Create the file if it doesn't exist
            print(f"HTML file created: {file_path}")
        else:
            print(f"HTML file already exists: {file_path}")

        # Generate the absolute path as a URI for opening
        abs_path = file_path.resolve().as_uri()

        # Print the link to allow copying and pasting in a browser
        print(f"Link to open the HTML file: {abs_path}")

        # Optionally, open the file directly in the web browser
        webbrowser.open(abs_path)


def build_graph(data):
    # Build a graph from the provided data (edges and weights)
    graph = nx.Graph()
    graph.add_weighted_edges_from(data)
    return graph
