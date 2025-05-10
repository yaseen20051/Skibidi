import networkx as nx
import matplotlib.pyplot as plt


def draw(adj_list, high_adj, i):
    # define main graph
    if i == -1:
        return
    G = nx.Graph()

    for node, neighbors in adj_list.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    # define highlighted
    G2 = nx.Graph()

    for node, neighbors in high_adj.items():
        for neighbor, weight in neighbors:
            G2.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, k=1.5)

    highlight_nodes = G2.nodes
    all_nodes = G.nodes()
    highlight_edges = G2.edges

    # highlight specified nodes
    node_colors = ["orange" if n in highlight_nodes else "lightblue" for n in all_nodes]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', node_size=2000, font_size=16)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=20)

# Highlight label
    ax = plt.gca()
    for (u, v) in highlight_edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]

        mx, my = (x1 + x2) / 2, (y1 + y2) / 2

        label = f"{G[u][v]['weight']}"

        circle = plt.Circle((mx, my), 0.06, color="yellow", zorder=1)
        ax.add_patch(circle)

        plt.text(mx, my, label, fontsize=12, ha="center", va="center", color="blue", zorder=2, fontweight="bold")

    plt.title("Highlighted Edges with Circled Labels")
    plt.savefig(f"graphs/graph{i}.png", format="png", dpi=300)
    plt.clf()


#print(adj_list)