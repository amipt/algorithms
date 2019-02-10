from AdjacencyMatrixGraph import AdjacencyMatrixGraph
from AdjacencySetGraph import AdjacencySetGraph
import display
import traverse
import numpy as np
# # un-directed graph
# print("*"*10,"un-directed AdjacencyMatrixGraph","*"*10)
# gud = AdjacencyMatrixGraph(4)
# gud.add_edge(0, 1)
# gud.add_edge(0, 2)
# gud.add_edge(2, 3)

# display.display(gud, 4)

# # directed graph
# print("*"*10,"directed AdjacencyMatrixGraph","*"*10)
# gd = AdjacencyMatrixGraph(4, directed=True)
# gd.add_edge(0, 1)
# gd.add_edge(0, 2)
# gd.add_edge(2, 3)
# display.display(gd, 4)

# # un-directed graph
# print("*"*10,"un-directed AdjacencySetGraph","*"*10)
# gud = AdjacencySetGraph(4)
# gud.add_edge(0, 1)
# gud.add_edge(0, 2)
# gud.add_edge(2, 3)

# display.display(gud, 4)

print("*"*10,"directed AdjacencySetGraph","*"*10)
gud = AdjacencySetGraph(9,directed=False)
gud.add_edge(0, 1)
gud.add_edge(1, 2)
gud.add_edge(2, 7)
gud.add_edge(2, 4)
gud.add_edge(2, 3)
gud.add_edge(1, 5)
gud.add_edge(5, 6)
gud.add_edge(6, 3)
gud.add_edge(3, 4)
gud.add_edge(6, 8)

#display.display(gud, 4)

# traverse.breadth_first(gud,2)
visted = np.zeros(gud.numVertices)
traverse.depth_first(gud,visted,2)

print("*"*10,"directed AdjacencyMatrixGraph","*"*10)
gr = AdjacencyMatrixGraph(9,directed=True)
gr.add_edge(0, 1)
gr.add_edge(1, 2)
gr.add_edge(2, 7)
gr.add_edge(2, 4)
gr.add_edge(2, 3)
gr.add_edge(1, 5)
gr.add_edge(5, 6)
gr.add_edge(3, 6)
gr.add_edge(3, 4)
gr.add_edge(6, 8)

traverse.topological_sort(gr)


print("*"*10,"shortest un directed AdjacencySetGraph","*"*10)
gr = AdjacencySetGraph(8,directed=False)
gr.add_edge(0, 1)
gr.add_edge(1, 2)
gr.add_edge(1, 3)
gr.add_edge(2, 3)
gr.add_edge(1, 4)
gr.add_edge(3, 5)
gr.add_edge(5, 4)
gr.add_edge(3, 6)
gr.add_edge(6, 7)
gr.add_edge(0, 7)
traverse.shortest_path(gr,0,5)
traverse.shortest_path(gr,0,6)
traverse.shortest_path(gr,7,4)

print("*"*10,"shortest directed AdjacencySetGraph","*"*10)
gr = AdjacencySetGraph(8,directed=True)
gr.add_edge(0, 1)
gr.add_edge(1, 2)
gr.add_edge(1, 3)
gr.add_edge(2, 3)
gr.add_edge(1, 4)
gr.add_edge(3, 5)
gr.add_edge(5, 4)
gr.add_edge(3, 6)
gr.add_edge(6, 7)
gr.add_edge(0, 7)
distance_table = traverse.build_distance_table(gr,0)
for vId, vertex in distance_table.items():
    print(vId,vertex)
traverse.shortest_path(gr,0,5)
traverse.shortest_path(gr,0,6)
traverse.shortest_path(gr,7,4)