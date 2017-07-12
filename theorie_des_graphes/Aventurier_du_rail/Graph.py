#!/usr/bin/env python3

#-*- coding: utf-8 -*-

##############################################
# Institut Villebon, UE OP.5.i04             #
# Simple class to represent graphs           #
# Version 1                                  #
# Author :                                   #
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

    def __repr__(self):
        """ convert to a string the current instance """
        edges = [edge for edge in self.edges]
        announce = "************************\n" + \
                   "* Display of the map *\n" + \
                   "************************\n"
        edges = "Lien :\n_______\n\n" + '\n'.join([edge[0] + " -" + edge[2] + "-> " + edge[1] + "color : " + edge[3] \
                                                    for edge in edges]) + '\n'
        separation = "========================="
        return announce + edges + separation

    def add_a_node(self, node_name):
        """ Add a node to the current instance.

        :Param name: String which represents the name of the new node

        Remark: Nothing is created if there already exists a node with the same name
        """
        self.nodes.add(node_name)
        self.adjacency_list[node_name] = []

    def add_an_edge(self, from_node, to_node, value, color):
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
                self.edges.append((from_node, to_node, value, color))
                self.edges.append((to_node, from_node, value, color))
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



if __name__ == '__main__':
    G = Graph()
    G.add_a_node('(0, 0)')
    G.add_a_node('(0, 1)')
    G.add_a_node('(0, 2)')
    G.add_a_node('(1, 0)')
    G.add_a_node('(1, 1)')
    G.add_a_node('(1, 2)')
    G.add_a_node('(2, 0)')
    G.add_a_node('(2, 1)')
    G.add_a_node('(2, 2)')
    G.add_an_edge('(0, 1)', '(0, 0)', 3)
    G.add_an_edge('(0, 2)', '(0, 0)', 2)
    G.add_an_edge('(0, 2)', '(0, 1)', 3)
    G.add_an_edge('(1, 0)', '(0, 0)', 5)
    G.add_an_edge('(1, 1)', '(0, 1)', 10)
    G.add_an_edge('(1, 1)', '(1, 0)', 2)
    G.add_an_edge('(1, 2)', '(0, 2)', 5)
    G.add_an_edge('(1, 2)', '(1, 0)', 8)
    G.add_an_edge('(1, 2)', '(1, 1)', 9)
    print(G.breadth_first_search('(0, 0)'))
