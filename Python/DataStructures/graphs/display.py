def display(gr, numVertices):
    for i in range(numVertices):
        print("Adjacent to :: ", i, gr.get_adjacent_vertices(i))
    for i in range(numVertices):
        print("Indegree :: ", i, gr.get_indegree(i))
    for i in range(numVertices):
        for j in gr.get_adjacent_vertices(i):
            print("Edge weight from %d to %d, weight: %.2f" %
                  (i, j, gr.get_edge_weight(i, j)))

    gr.display()