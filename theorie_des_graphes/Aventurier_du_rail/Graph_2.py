#!/usr/bin/env python3

#-*- coding: utf-8 -*-

##############################################
# Institut Villebon, UE OP.5.i04             #
# Simple class to represent graphs           #
# Version 1                                  #
# Authors :   Antoine et Lauren              #
##############################################

class Graph:
    """ Class that allows to define and construct an oriented graphs
    The graph is represented by the set of its nodes and the list of all
    its edges and knows its adjacency list.
    
    These class has three attributes:
    :Attribute nodes: Set of String, which represents the set of nodes
                      of the graph
    :Attribute edges: List of couple of String, which represents
                      the set of edges of the graph
    :Attribute adjacency_list: Dict which represents the adjacency list
                               of the graph, i.e. whose keys are the nodes
                               of the graph and whose values are the neighbors
                               of the key
    """

    def __init__(self):
        """ Constructor of the Graph class, which can only construct an empty
        graph

        Attributes: nodes, of type Set
                    adjacency_list, of type Dict

        Example:
        --------
        >>> Graph()
        """
        self.nodes = set()
        self.edges = list()
        self.adjacency_list = {}
        self.distances = {}

    def __repr__(self):
        """ convert to a string the current instance """
        edges = [edge for edge in self.edges]
        announce = "************************\n" + \
                   "* Display of the graph *\n" + \
                   "************************\n"
        nodes = "Nodes :\n_______\n\n" + ', '.join([node for node in self.nodes]) + \
                "\n" * 2
        edges = "Egdes :\n_______\n\n" + '\n'.join([edge[0] + " ---> " + edge[1] \
                                                    for edge in edges]) + '\n'
        separation = "========================="
        return announce + nodes + edges + separation

    def add_a_node(self, node_name):
        """ Add a node to the current instance.

        :Param name: String which represents the name of the new node

        Remark: Nothing is created if there already exists a node with the same name
        """
        self.nodes.add(node_name)
        self.adjacency_list[node_name] = []

    def add_an_edge(self, from_node, to_node, value):
        """ Add an edge to a graph if from_node and to_node are some nodes
        of the current graph

        :Param from_node: String which represents the name of the origin of the 
                          the edge which is currently added to the current instance
        :Param to_node: String which represents the name of the ending of the edge
                        which is currently added to the current instance

        Remark: Nothing is created if one of the node is not created yet
        """
        if from_node in self.nodes:
            if to_node in self.nodes:
                self.adjacency_list[from_node].append(to_node)
                self.adjacency_list[to_node].append(from_node)
                self.edges.append((from_node, to_node, value))
                self.edges.append((to_node, from_node, value))
                self.distances[str((from_node, to_node))] = value
                self.distances[str((to_node, from_node))] = value
            else:
                raise NameError("The node " + to_node + " is not created yet")
        else:
            raise NameError("The node " + from_node + " is not created yet")

    def is_non_oriented(self):
        """ Check if the current graph is oriented

        :Return values: Boolean
        """
        for node in self.nodes:
            neighbors = self.adjacency_list[node]
            for neighbor in neighbors:
                if node not in self.adjacency_list[neighbor]:
                    return False
        return True
        
    def breadth_first_search(self, departure):
        """
        return a dictionnary that have node as key and node as value 
        the node in value is the parent of the node in the key
        
        use the fifo methode to determine which one is the next to look at.
        
            departure is the first starting point of the course
        """
        colors = {}
        for node in self.nodes:
            colors[node] = "white"
            
        parents = {}
        fifo = [departure]
        colors[departure] = "grey"
        parents[departure] = None
        
        for node in sorted(self.nodes):

            while fifo != []:
                in_progress = fifo.pop(0)
                for neighbour \
                        in sorted(self.adjacency_list[in_progress]):
                    if colors[neighbour] == "white":
                        parents[neighbour] = in_progress
                        colors[neighbour] = "grey"
                        fifo.append(neighbour)
                colors[in_progress] = "black"
                
                
            
            if colors[node] != "white":
                continue
            colors[node] = "grey"
            parents[node] = None
            fifo.append(node)
            
        return parents

    def min_parent(self, parent_1, parent_2, l_min):
        """ method that returns the shortest path from parents nodes"""
        if l_min[parent_1] < l_min[parent_2] + self.distances[str((parent_1,parent_2))]:
            return l_min[parent_1], parent_1
        else:
            return l_min[parent_2] + self.distances[str((parent_1,parent_2))], parent_2
       
    def dijkstra(self, departure):
        """ returns the shortest path """
        visited = [departure]  # liste qui contiendra les sommets visités
        unvisited =  []        # liste contenantles sommets non visités
        path = {}               # dico qui indiquera le chemin le plus court suivi
        l_min = {}
        color = {}
        for s in self.nodes:        # for s in S
            l_min[s] = float('inf')    # on initialise tous les sommets de l=inf
            color[s] = 1              
            path[s] = []              # liste qui contiendra le chemin suivi
        color[departure] = 0
        l_min[departure] = 0         
        path[departure] = None
        unvisited.append(departure)
        for v in self.adjacency_list[departure]:
            if not v in unvisited:
                l_min[v] = self.distances[str((departure, v))]
                unvisited.append(v)
        

        while len(unvisited) != 0 :
            s_min = unvisited[0]          
            for s in unvisited:
                if l_min[s] < l_min[s_min]:
                    s_min = s           # sommet non visité ayant la plus petite value

            for v in self.adjacency_list[s_min]:
                if color[v] != 0:
                    l_min[v], new_v = self.min_parent(v, s_min, l_min)
                    if v != new_v:
                        path[v] = new_v
                    if not v in unvisited:
                        unvisited.append(v)
                    
            color[s_min] = 0               
            unvisited.remove(s_min)
            visited.append(s_min)

        return l_min, path
  
            


if __name__ == '__main__':
    G = Graph()
    fileh = open("fichiercsv/cartes_bretagne_-_version_epuree.csv", encoding = "UTF-8")
    lines = [line[:-1].split(":") for line in fileh][1:]
    fileh.close()
    for line in lines:
        if not line[0] in G.nodes:
            G.add_a_node(line[0])
        if not line[1] in G.nodes:
            G.add_a_node(line[1])
        G.add_an_edge(line[0], line[1], int(line[2]))

    d, v = G.dijkstra('Brest')
    """  RESTART: C:\Users\charpak2.33\Documents\GitHub\Aventurier_du_rail\Graph_2.py 
        >>> d
        {'Dinan': 13, 'Ploërmel': 11, 'Lorient': 7, 'Rennes': 15, 'Saint Malo': 14, 'Carhaix': 5,
        'Quimper': 3, 'Brest': 0, 'Vannes': 10, 'Perros-Guirec': 5, 'Pontivy': 8}
        >>> v
        {'Dinan': 'Pontivy', 'Ploërmel': 'Pontivy', 'Lorient': 'Quimper', 'Rennes': 'Ploërmel','Saint Malo': 'Dinan',
        'Carhaix': 'Brest', 'Quimper': 'Brest', 'Brest': None, 'Vannes': 'Lorient', 'Perros-Guirec': 'Brest', 'Pontivy': 'Carhaix'}
    """
