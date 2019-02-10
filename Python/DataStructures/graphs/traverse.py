#!~/data/python/anaconda/bin/python

from AdjacencyMatrixGraph import AdjacencyMatrixGraph
from AdjacencySetGraph import AdjacencySetGraph
from queue import Queue
import numpy as np
import time


def breadth_first(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue
        print("Visited", vertex)
        visited[vertex] = 1
        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)


def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return
    print("Visited:", current)
    visited[current] = 1
    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)


def topological_sort(graph):
    queue = Queue()
    indegreeMap = {}

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)
        # print("indegree for vertex %d :: %d"%(i,graph.get_indegree(i)))

        if indegreeMap[i] == 0:
            queue.put(i)
    sortedList = []
    while not queue.empty():
        vertex = queue.get()

        sortedList.append(vertex)
        for v in graph.get_adjacent_vertices(vertex):
            indegreeMap[v] = indegreeMap[v] - 1
            if indegreeMap[v] == 0:
                queue.put(v)
    if len(sortedList) != graph.numVertices:
        raise ValueError("this graph has a cycle...")
    print(sortedList)


def build_distance_table(graph, source):
    distance_table = {}
    for i in range(graph.numVertices):
        distance_table[i] = (None, None)
    distance_table[source] = (0, source)

    queue = Queue()
    queue.put(source)
    while not queue.empty():
        currrent_vertex = queue.get()
        currrent_distance = distance_table[currrent_vertex][0]

        for neigbour in graph.get_adjacent_vertices(currrent_vertex):

            if distance_table[neigbour][0] is None:
                distance_table[neigbour] = (
                    currrent_distance+1, currrent_vertex)

                if len(graph.get_adjacent_vertices(neigbour)) > 0:
                    queue.put(neigbour)
    return distance_table


def shortest_path(graph, source, destination):
    distance_table = build_distance_table(graph, source)
    path = [destination]
    
    previous_vertex = distance_table[destination][1]
    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]
    if previous_vertex is None:
        print("There is no path from source: %d to destination: %d" %
              (source, destination))
    else:
        path = [source] + path
        print("shortest path ::", path)
