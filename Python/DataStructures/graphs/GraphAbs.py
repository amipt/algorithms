#!~/data/python/anaconda/bin/python

import abc


class Graph(abc.ABC):
    '''
        numVertices: number of nodes or vertices
        directed: wether the graph is directed or undirected
    '''
    def __init__(self,numVertices,directred=False):
        self.numVertices = numVertices
        self.directred = directred
    
    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass
    
    @abc.abstractmethod
    def get_adjacent_vertices(self,v):
        pass
    
    @abc.abstractmethod
    def get_indegree(self,v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass
    
    @abc.abstractmethod
    def display(self):
        pass