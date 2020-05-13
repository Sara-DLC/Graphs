# from Graph file
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_ancestors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise Exception("Vertex not found")

# From Util file


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
# check vertex in ancestors
    for v in ancestors:
        # add vertex at 0 and 1 as well as edges add_vertex takes one argument
        graph.add_vertex(v[0])
        graph.add_vertex(v[1])

        graph.add_edge(v[1], v[0])
    # create queue, starting length and earliest_ancestor
    queue = Queue()
    queue.enqueue([starting_node])
    length = 1
    earliest_ancestor = -1
    # while queue is empty check if the length of the path is greater than/equal to the length and vertex is less than earliest_ancestor otherwise check if length of the path is greater than the length of 1
    while queue.size() > 0:
        path = queue.dequeue()
        v = path[-1]

        if (len(path) >= length and v < earliest_ancestor) or (len(path) > length):
            earliest_ancestor = v
            length = len(path)
        # got help with this part still a bit confused but tests pass
        # current understanding for every neighboring vertex in the graph vertices set append its neighbor and cue the path.
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            queue.enqueue(path_copy)

    return earliest_ancestor
