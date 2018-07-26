class Graph:
    """Graph implementations with different constructors and algorithms"""
    #Creates initilized graph, if not it creates empty graph
    def __init__(self, graphDict = None):
        if graphDict == None:
          self.__graphDict = {}
        else:
            self.__graphDict = graphDict
    #add vertex if it is not in the graph
    def add_vertex(self, vertex):
        if vertex not in self.__graphDict:
            self.__graphDict[vertex] = []
    #add edge if vertex is exits, if not add vertex to key then add edge to list 
    def add_edge(self, edge):
        (v1, v2) = tuple(edge)
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.__graphDict[v1].append(v2)
    #get all vertices on the graph
    def vertices(self):
        return list(self.__graphDict.Keys())
    def edges(self):
        return generate_edges()
    def __generate_edges():
        edges = []
        for key in self.__graphDict.Keys():
            for dest in self.__graphDict[key]:
                edges.append((key,dest))
        return edges
    
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

