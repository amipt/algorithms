#!~/data/python/anaconda/bin/python

from GraphAbs import Graph
import display

class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError(
                "The vertex %d can not be adjacent to itself" % (v))
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencySetGraph, self).__init__(numVertices, directed)
        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append(Node(i))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError(
                "Vertices %d or/and %d are out of bounds" % (v1, v2))
        self.vertex_list[v1].add_edge(v2)
        if self.directred == False:
            self.vertex_list[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):
        if v >= self.numVertices or v < 0:
            raise ValueError("Vertex %d not in valid range" % (v))
        return self.vertex_list[v].get_adjacent_vertices()

    def get_indegree(self, v):
        if v >= self.numVertices or v < 0:
            raise ValueError("Vertex %d not in valid range" % (v))
        indegree = 0
        for i in range(self.numVertices):
            if v in self.vertex_list[i].get_adjacent_vertices():
                indegree += 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for i in range(self.numVertices):
            for j in self.get_adjacent_vertices(i):
                print(i, "-->", j)