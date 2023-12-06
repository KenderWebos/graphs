import networkx as nx
import matplotlib.pyplot as plt

# Crear un MultiGraph
MG = nx.MultiGraph()

# Agregar nodos
MG.add_nodes_from([1, 2, 3, 4])

# Agregar conexiones con múltiples aristas entre los mismos nodos
MG.add_edge(1, 2)
MG.add_edge(1, 2)
MG.add_edge(1, 2)
MG.add_edge(2, 3)
MG.add_edge(3, 4)
MG.add_edge(3, 4)
MG.add_edge(3, 4)

# Dibujar el MultiGraph
nx.draw(MG, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
plt.show()
