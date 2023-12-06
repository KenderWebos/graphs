import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo
G = nx.DiGraph()

# Agregar nodos

G.add_nodes_from(["A", "B", "C", "D"])
# G.add_nodes_from([1, 2, 3, 4])

# Agregar conexiones entre nodos (aristas)

# G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 2)])
G.add_edges_from([("A", "B"), ("B", "C"), ("C", "D"), ("A", "A")])

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
plt.show()
