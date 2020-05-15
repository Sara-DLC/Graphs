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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('No Vertex found')

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
        # start an empty queue
        q = Queue()
        # add the starting vertex to the empty queue
        q.enqueue(starting_vertex)
        # start a set of visited vertexes
        visited = set()

        # while the queue is not empty add vertices visited to the set
        while q.size() > 0:
            # removes vertices from the queue
            v = q.dequeue()
            # if the vertex has not been visited (if not in the set) print the vertex and add it to the set since it is now visited.
            if v not in visited:
                print(v)
                visited.add(v)
                # look for next connected vertex and add it to the queue (line 51 checks for visited)
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # start an empty stack
        q = Stack()
        # add (push) the starting vertex to the empty stack
        q.push(starting_vertex)
        # start a set of visited vertices
        visited = set()

        # while the queue is not empty add vertices visited to the set
        while q.size() > 0:
            # removes (pops) vertices from the queue
            v = q.pop()
            # if the vertex has not been visited (if not in the set) print the vertex and add it to the set since it is now visited.
            if v not in visited:
                print(v)
                visited.add(v)
                # look for next connected vertex and add it to the queue (line 51 checks for visited)
                for next_vertex in self.get_neighbors(v):
                    q.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Sets visited to an empty set if None
        if not visited:
            visited = set()
        # if starting vertex has not been visited print said vertex and add it to the visited set
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            # check neighbor of the starting vertex and recursively add the neighbors and visited
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last_item = path[-1]

            if last_item not in visited:
                visited.add(last_item)

                if last_item is destination_vertex:
                    return path

                for neighbor in self.get_neighbors(last_item):
                    q.enqueue([*path, neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            path = stack.pop()
            last_item = path[-1]

            if last_item not in visited:
                visited.add(last_item)

                if last_item is destination_vertex:
                    return path
                # Once all neighbors have both been ran through, push args
                for neighbor in self.get_neighbors(last_item):
                    stack.push([*path, neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Sets visited to an empty set if None
        if visited is None:
            visited = set()

        # if starting vertex visited don't do anything
        if starting_vertex in visited:
            return None

        # if it has been visited add to visited set
        visited.add(starting_vertex)

        # if the starting vertices and the destination_vertex match, return the index of starting_vertex
        if starting_vertex is destination_vertex:
            return [starting_vertex]

        # goes through all the neighbors and runs the function recursively(again)
        for neighbor in self.get_neighbors(starting_vertex):
            path = self.dfs_recursive(neighbor, destination_vertex, visited)

            # Once path and destination_vertex have both been ran through, return all args
            if path and destination_vertex in path:
                return [starting_vertex, *path]


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
