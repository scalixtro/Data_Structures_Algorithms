class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        """
        Add a new node to the graph.

        Keyword Arguments:
            - vertex: Value / Name of the new vertex.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        """
        Add a new edge between two vertices v1 and v2.
        """
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        """
        Removes an edge between two vertices v1 and v2.
        """
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        """
        Removes a given vertex from the graph. This method is considering
        bidirectional edges between all nodes.
        """
        # Check if vertex is in the graph
        if vertex in self.adj_list.keys():
            # For each connection of vertex, remove vertex from those
            # lists
            connected_nodes = self.adj_list[vertex]
            for connected_node in self.adj_list[vertex]:
                self.adj_list[connected_node].remove(vertex)
            # Finally delete the vertex
            del self.adj_list[vertex]
            return True
        return False