# Graphs

Los grafos son estructuras matemáticas utilizadas para representar relaciones entre objetos. Consisten en nodos (también llamados vértices) que están conectados por aristas (también llamadas bordes). Los grafos son una herramienta poderosa para modelar una amplia gama de problemas en ciencias de la computación, matemáticas y otras disciplinas.

# Tipos de Grafos
Existen diferentes tipos de grafos:

* Grafo no dirigido: Las aristas no tienen dirección, lo que significa que la conexión entre nodos es bidireccional.
* Grafo dirigido: Las aristas tienen dirección, indicando una relación unidireccional entre nodos.
* Grafo ponderado: Asocia un peso o valor a cada arista.
* Grafo cíclico: Contiene al menos un ciclo, es decir, un camino cerrado que comienza y termina en el mismo nodo.
* Grafo acíclico: No contiene ciclos.

# Representacion en programacion usando python y NetworkX

Representaremos un grafo direccional usando python y networkX

```py
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

```

# Conclusion

