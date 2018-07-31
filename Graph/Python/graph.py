# This class represents a directed graph
# using adjacency list representation
class Graph:
    
    #Creates initilized graph, if not it creates empty graph
    def __init__(self, graphDict = None):
        if graphDict == None:
            self.__graph = {}
            self.__vertices = []
            self.__edges = []
        else:
            self.__graph = graphDict
            self.__vertices = list(self.__graph.keys())
            self.__edges = []
            self.__generate_edges()
    #add vertex if it is not in the graph
    def add_vertex(self, vertex):
        if vertex not in self.__vertices:
            self.__graph[vertex] = []
            self.__vertices.append(vertex)
    #add edge if vertex is exits, if not add vertex to key then add edge to list 
    def add_edge(self, u,v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.__graph[u].append(v)
        self.__edges.append((u,v))
    #get all vertices on the graph
    def vertices(self):
        return self.__vertices
    #Get all edges on the graph
    def edges(self):
        return self.__edges
    #Private function to generate all edges given graph
    def __generate_edges(self):
        for key in self.__vertices:
            for dest in self.__graph[key]:
                self.__edges.append((key,dest))

    #Returns BFS list of graph
    def bfs(self,start):
        #Mark all vertex as visited
        visited = {v: False for v in self.__vertices}

        bfs_tree = [] 
        #Setup first node
        queue = [start]
        visited[start] = True
        
        #iterate over queue
        while queue:
            #dequeue first node and put it bfs
            el = queue.pop(0)
            bfs_tree.append(el)
            
            #take all adjacency vertices into queue if is not visited
            for ad in self.__graph[el]:
                if not visited[ad]:
                    queue.append(ad)
                    visited[ad] = True
    
        return bfs_tree
    
    #Return list of DFS tree from given node
    def dfs(self,start):
        visited = {v: False for v in self.__vertices}
        
        dfs_tree = []
        #Setup first node
        stack = [start]

        #iterate over stack and add vertices to stack if it is not visited
        while stack:
            el = stack.pop(-1)
            dfs_tree.append(el)
            visited[el] = True

            for ad in self.__graph[el]:
                if not visited[ad]:
                    stack.append(ad)

        return dfs_tree
    #Rcursive function for topological sort to find deepest vertices
    def __topological_sort_util(self, v, visited, top_stack):
        #Mark v vertex as visited
        visited[v] = True

        for u in self.__graph[v]:
            if visited[u] == False:
                self.__topological_sort_util(u,visited,top_stack)
        
        #add vertex which its indegree is zero
        top_stack.insert(0,v)

        
        
    #return topological sort of graph
    def topological_sort(self):
        #Mark all verticies as unvisited
        visited = {v: False for v in self.__vertices}
        #Create stack to keep trrack of vertices
        top_stack = []
        
        #Iterate over all vertices if it is unvisited call recursive util func
        for v in self.__vertices:
            if visited[v] == False:
                self.__topological_sort_util(v,visited,top_stack)
        return top_stack

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

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())

    print("BFS of graph:")
    print(graph.bfs('e'))

    print("DFS of graph:")
    print(graph.dfs('e'))

    print("Topological sort of graph:")
    print(graph.topological_sort())