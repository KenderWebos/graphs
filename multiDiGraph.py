import networkx as nx
import matplotlib.pyplot as plt

# Crear un MultiDiGraph
MDG = nx.MultiDiGraph()

# Agregar nodos
MDG.add_nodes_from([1, 2, 3, 4])

# Agregar conexiones con múltiples aristas dirigidas entre los mismos nodos
MDG.add_edge(1, 2)
MDG.add_edge(1, 2)
MDG.add_edge(2, 1)
MDG.add_edge(2, 3)
MDG.add_edge(3, 4)
MDG.add_edge(3, 4)
MDG.add_edge(3, 4)

# Dibujar el MultiDiGraph
nx.draw(MDG, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold', arrows=True)
plt.show()
