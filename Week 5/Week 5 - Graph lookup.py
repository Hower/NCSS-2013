from node import Node
class ParseException:
  pass

class Graph:

    def __init__(self, label, filename):
        """
        Initialise a graph with a given label.
        If filename is not None, load the graph from the file
        """
        self.label = label
        self.graph = {}
        if filename:
            self.load(filename)

    def size(self):
        """
        Return the number of nodes in the graph
        """
        return len(self.graph)

    def load(self, filename):
        """
        Load the graph from the given filename.
        Raise ValueError if a node with a duplicate
        id is added or if a relationship between
        nonexisting nodes is created
        """
        flag = False
        for line in open(filename, 'r'):
            line = line.strip()

            # if line is empty, set flag to start building relationships
            if not line:
                flag = True
                continue

            # build nodes
            if flag is False:
                id, label = line.split(":")
                label = label[1:]
                # if already in graph
                if id in self.graph:
                    raise ValueError
                self.graph[id] = Node(id, label)

            # build relationships
            else:
                from_id, label, neighbour_id = line.split(':')
                if from_id not in self.graph or neighbour_id not in self.graph:
                    raise ValueError
                if not label:
                    label = None
                for node in self.graph:
                    if self.graph[node].id == from_id:
                        # Pointers FTWWWWWWW
                        self.graph[node].add_neighbour(self.graph[neighbour_id], label)

    def output(self):
        """
        Prints the graph with nodes listed in sorted order
        of ids with their neighbours and neighbour labels
        If neighbour labels are None, print the empty
        string.
        Print empty brackets if a node has no neighbours
        e.g.
        (0: Bob) [1:son, 2:wife]
        (1: John) [0:father, 2:mother]
        (2: Jane) [0:husba  nd, 1:son]
        (3: Greg) [1:friend]
        """
        for node in sorted(self.graph):
            out = []
            for label in self.graph[node].neighbours:
                for each in self.graph[node].neighbours[label]:
                    if not label:
                        label = ""
                    out.append((each.id, label))

            out.sort(key=lambda x: x[0])
            real = ""

            for relation in out:
                real += "{}:{}".format(relation[0], relation[1]) + ', '

            real = "[" + real[:-2] + "]"
            print("{} {}".format(self.graph[node], real))

    def degrees_of_separation(self, n1, n2):
        """
        Returns the minimum degrees of separation from
        n1 to n2, where n1 and n2 are ids.
        Each x on the path between n1
        and n2 fulfills the has_neighbour relationship.
        Return -1 if n1 and n2 are not connected.
        Raise ValueError if either n1 or n2 is not in
        this graph
        If n2 is a neighbour of n1, then there is
        1 degree of separation.
        e.g. graph.degrees_of_separation(n1, n2)
        """
        if n1 not in self.graph or n2 not in self.graph:
            raise ValueError

        # BFS search
        total = 0
        toDo = [(n1, total)]
        visited = []
        while toDo:
            current, total = toDo.pop(0)
            neighs = self.graph[current].get_neighbours(None)
            if current == n2:
                break
            total += 1
            if current in visited:
                continue
            visited.append(current)
            for neigh in neighs:
                toDo.append((neigh.id, total))
        else:
            return -1
        return total

    def get_node(self, id):
        """
        Returns the node with the given id
        Raise ValueError if no node with the id exists
        """
        if id not in self.graph:
            raise ValueError
        else:
            return self.graph[id]

    def graph_seach(self, node, query):

        string = "NEIGHBOURS WHO HAVE LABEL bob".split()
        if len(string) < 3:
          raise IndexError
        start = string[:3]
        if ' '.join(start) == "NEIGHBOURS WHO HAVE":

        elif ' '.join(start) == "PEOPLE WHO HAVE":
          pass
        elif ' '.join(start) == "ALL NEIGHBOURS":
          return self.graph[current].get_neighbours(None)
        else:
          raise IndexError