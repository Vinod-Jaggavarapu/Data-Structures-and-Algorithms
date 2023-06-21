class Node:
    def __init__(self,vertex):
        self.vertex = vertex
        self.next = None

class Graph:
    def __init__(self,size):
        self.graph = [None]*size
    
    def add_edge(self,source,destination):
        #Undirected Graph

        node =Node(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = Node(source)
        node.next = self.graph[destination]
        self.graph[destination]=node
    
    def print_graph(self):
        for index,addr in enumerate(self.graph):
            temp = addr
            print(index,end="---> ")
            while temp !=None:
                print(temp.vertex,end=" ")
                temp = temp.next
            print("\n")

g= Graph(4)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)

g.print_graph()
            
            
