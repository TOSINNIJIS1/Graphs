"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Sprint
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('exception')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
            else:
                q.dequeue()

            w = self.vertices[v]
            for i in w:
                if i not in visited:
                    q.enqueue(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a queue
        stack = Stack()

        # make a set to track which nodes we have visited
        visited = set()

        # push on the starting node
        stack.push(starting_vertex)

        # loop while the stack isn't empty
        while stack.size() > 0:
            # pop, this is our current node
            current_node = stack.pop()

            # check if we've yet visited
            if current_node not in visited:
                print(current_node)
            ## if not, we go to the node
            ### mark as visited == add to visited set
                visited.add(current_node)

            ### get the neighbors
                neighbors = self.get_neighbors(current_node)
            ### iterate over the neighbors, enqueue them
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
    
            visited.add(starting_vertex)

            neighbors = self.get_neighbors(starting_vertex)
            if len(neighbors) == 0:
                return

            else:
                for neighbor in neighbors:
                    self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()

        # make a set to track which nodes we have visited
        visited = set()

        # enqueue the PATH TO the starting node
        q.enqueue([starting_vertex])

        # loop while the queue isn't empty
        while q.size() > 0:
            # dequeue, this is our current path
            current_path = q.dequeue()
            current_node = current_path[-1]

            # check if we have found our target node
            if current_node == destination_vertex:
                # then we are done! return
                return current_path

            # check if we've yet visited
            if current_node not in visited:
            ## if not, we go to the node
            ### mark as visited == add to visited set
                visited.add(current_node)

            ### get the neighbors
                neighbors = self.get_neighbors(current_node)
            ### iterate over the neighbors, enqueue the PATH to them
                for neighbor in neighbors:
                    # path_copy = list(current_path)
                    # path_copy = current_path.copy()
                    # path_copy = copy.copy(current_path)
                    # path_copy = current_path[:]​
                    # path_copy.append(neighbor)
                    path_copy = current_path + [neighbor]

                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
         # Create an empty stack
        path = Stack()

        # Add the starting vertex to the path
        path.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        #  Add the starting vertex to the set
        visited.add(starting_vertex)

        # Loop while the stack is not empty
        while path.size() > 0:
            # Pop the first element
            new_edge = path.pop()
            # Add the popped element to the visited set
            visited.add(new_edge)

            # Get all neighbors
            neighbors = self.get_neighbors(new_edge)

           # Put all the neighbors on the stack
            for neighbor in neighbors:
                if neighbor not in visited:
                   path.push(neighbor)
                if neighbor is destination_vertex:
                    visited.add(neighbor)
                    return list(visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(path) == 0:
            path.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path

        if starting_vertex not in visited:
            visited.add(starting_vertex)
        
            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                path_copy = path + [neighbor]
                # only return if we found the destination_vertex
                result = self.dfs_recursive(neighbor, destination_vertex, path_copy, visited)
                if result is not None:
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    graph.add_edge('0', '4')

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

