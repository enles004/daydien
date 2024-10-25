import matplotlib
import networkx as nx

matplotlib.use('Agg')
import matplotlib.pyplot as plt


def draw_mst(N, mst_edges):
    G = nx.Graph()
    for i in range(N):
        G.add_node(i)
    for u, v, length in mst_edges:
        G.add_edge(u, v, weight=length)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.savefig('./static/mst_graph.png')
    plt.close()
