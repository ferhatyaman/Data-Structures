class Graph:
    """Graph implementations with different constructors and algorithms"""
    #Creates initilized graph, if not it creates empty graph
    def __init__(self, graphDict = None):
        if graphDict == None:
            self.__graphDict = {}
            self.__vertices = []
            self.__edges = []
        else:
            self.__graphDict = graphDict
            self.__vertices = self.__graphDict.Keys()
            self.__generate_edges()
    #add vertex if it is not in the graph
    def add_vertex(self, vertex):
        if vertex not in self.__vertices:
            self.__graphDict[vertex] = []
            self.__vertices.append(vertex)
    #add edge if vertex is exits, if not add vertex to key then add edge to list 
    def add_edge(self, edge):
        (v1, v2) = tuple(edge)
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.__graphDict[v1].append(v2)
        self.__edges.append(tuple(edge))
    #get all vertices on the graph
    def vertices(self):
        return self.__vertices
    #Get all edges on the graph
    def edges(self):
        return self.__edges
    #Private function to generate all edges given graph
    def __generate_edges(self):
        for key in self.__vertices:
            for dest in self.__graphDict[key]:
                self.__edges.append((key,dest))

    def bfs(self,start):
        visited = {v: False for v in self.__vertices}
        queue = []
        bfs_tree = []
        queue.append(self.__graphDict[start])
        visited[start] = True
        bfs_tree.append(start)
        
        for el in queue:
            if not visited[el]:
                bfs_tree.append(el)
                visited[el] = True
                queue.append(self.__graphDict[el])

        print (bfs_tree)
    def dfs(self,start):
        visited = {v: False for v in self.__vertices}
        stack = []
        dfs_tree = []
        stack.append(self.__graphDict[start])
        visited[start] = True
        dfs_tree.append(start)
        for el in stack:
            if not visited[el]:
            dfs_tree.append(el)
            visited[el] = True
            stack.append(self.__graphDict[el])        
        
if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

