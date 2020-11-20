Graphs: are collections of data represented by nodes and connections between nodes.
All trees are Graphs but not all Graphs are trees

                        Components that are required to make up graphs:

Nodes or Verticles :- It represent objects in a data set (cities, animals, web page).

Edges :- Connections between veriticles; can be bidirectional. Note: Not all edges are not created equally. (How to get to the cites)

 
Weight :- Cost to travel across the edge. (Time to get to the cities, the length of the road, the longer the trip is. so the higher the weight the longer the trip)

                        Graphs is useful for 
Network Activity: for example 
:- It could show a collection of computers on a network.


                        Examples of Graphs
Directed Graph :- Can only move in one direction along edges
Undirected Graph :- Allows Movement in both directions along edges
Cyclic Graph :- Edges allow you to revisit at least one vert
Acyclic Graph :- Verticles can only be visited once

Matrix

class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B"},
                            "B": {"C", "D"},
                            "C": {"E"},
                            "D": {"F", "G"},
                            "E": {"C"},
                            "F": {"C"},
                            "G": {"A", "F"}
                        }

    A   B   C   D   E
A   0   1   0   0   0
B   1   0   1   1   1
C   0   1   0   1   0
D   0   1   1   0   0
E   0   1   0   0   0

class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]


Shorthand	Property
V	Total number of vertices in the graph
E	Total number of edges in the graph
e	Average number of edges per vertex