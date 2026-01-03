import os
import webbrowser
import networkx as nx
from pathlib import Path
from pyvis.network import Network

# 4 Levels: .../src/main/python_expert/networkx/__style_graphic__.py → root
PROJECT_ROOT = Path(__file__).resolve().parents[4]
OUTPUT_DIR = PROJECT_ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

theme_palette = {
    1: {"node": "#6C63FF", "edge": "#9D8CFF"},
    2: {"node": "#00D1B2", "edge": "#66E0D6"},
    3: {"node": "#FF7FBF", "edge": "#FFB0D1"},
    4: {"font": "#141414", "label": "#0A0A0A"}
}


def build_graph(data):
    graph = nx.Graph()
    graph.add_weighted_edges_from(data)
    return graph


class GraphStyle:
    edge_font_size = 10
    node_font_size = 25
    node_size = 30

    def __init__(
        self,
        node_color=theme_palette[1]["node"],
        node_font_color=theme_palette[4]["label"],
        edge_color=theme_palette[1]["edge"],
        edge_label_color=theme_palette[4]["font"]
    ):
        self.node_color = node_color
        self.node_font_color = node_font_color
        self.edge_color = edge_color
        self.edge_label_color = edge_label_color

    def draw_graph_pyvis(self, graph, title):
        net = Network(height="750px", width="100%", directed=False, notebook=False)

        for node in graph.nodes():
            net.add_node(
                node,
                label=node,
                color=self.node_color,
                font={'size': self.node_font_size, 'color': self.node_font_color, 'bold': True},
                size=self.node_size
            )

        for u, v, data_edge in graph.edges(data=True):
            weight = data_edge.get('weight', 1)
            net.add_edge(
                u, v,
                value=weight,
                width=weight,
                label=str(weight),
                title=f"Peso: {weight}",
                color=self.edge_color,
                font={'size': self.edge_font_size, 'color': self.edge_label_color}
            )

        net.show_buttons(filter_=['physics'])

        net.barnes_hut(
            spring_length=50,
            spring_strength=0.005,
            gravity=-2000,
            central_gravity=0.3,
            damping=0.09,
            overlap=0.1
        )

        file_name = f"{title.replace(' ', '_').lower()}.html"
        file_path = OUTPUT_DIR / file_name
        net.save_graph(str(file_path))

        abs_path = file_path.resolve().as_uri()
        print(f"\nHTML link")
        print(abs_path)
        webbrowser.open(abs_path)