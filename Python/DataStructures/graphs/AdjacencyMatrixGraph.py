#!~/data/python/anaconda/bin/python

from GraphAbs import Graph
import numpy as np
import display

class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((numVertices, numVertices))
    '''
        adds an edge between the vertices v1 and v2 with the given weight
    '''
    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError(
                "Vertices %d or/and %d are out of bounds" % (v1, v2))
        self.matrix[v1][v2] = weight

        if self.directred == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v >= self.numVertices or v < 0:
            raise ValueError("Vertex %d not in valid range" % (v))
        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] != 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_indegree(self, v):
        if v >= self.numVertices or v < 0:
            raise ValueError("Vertex %d not in valid range" % (v))
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] != 0.0:
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for j in self.get_adjacent_vertices(i):
                if self.matrix[i][j] != 0:
                    print(i, "-->", j)