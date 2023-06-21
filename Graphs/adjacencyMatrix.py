
class Graph:
    def __init__(self,size):
        self.adjMatrix =[]
        for i in range(size):
            self.adjMatrix.append([0 for j in range(size)])
    
    def add_edge(self,v1,v2):
        if v1 == v2:
            print("Both vertices are same")
            return
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2] ==0:
            print("There is no Edge between the vertices {} and {}".format(v1,v2))
            return
        self.adjMatrix[v1][v2]=0

    def print_matrix(self):
        for arr in self.adjMatrix:
            for ele in arr:
                print(ele, end=" ")
            print("\n")

g = Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)

g.print_matrix()
