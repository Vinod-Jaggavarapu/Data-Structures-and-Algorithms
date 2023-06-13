class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def buildBinarySearchTree(self,root,ele):
        if root ==None:
            return Node(ele)
        if ele < root.data:
            root.left = self.buildBinarySearchTree(root.left,ele)
        else:
            root.right = self.buildBinarySearchTree(root.right,ele)
        return root
    
    def countTotalNodes(self,root):
        if root ==None:
            return 0
        return 1+self.countTotalNodes(root.left)+self.countTotalNodes(root.right)
    
    def countLeafNodes(self,root):
        if root == None:
            return 0
        if root.left==None and root.right==None:
            #Only root node is present
            return 1
        return self.countLeafNodes(root.left)+self.countLeafNodes(root.right)
    
    def maxDepthOfTree(self,root):
        #Leetcode 104
        if root ==None:
            return 0
        else:
            ldepth = self.maxDepthOfTree(root.left)
            rdepth = self.maxDepthOfTree(root.right)
            return max(ldepth,rdepth)+1
    
    def maxDepthIterativeApproach(self,root):
        stack=[]
        depth =0
        if root:
            stack.append((1,root))          
            while stack:
                current_depth,root = stack.pop()
                print('current_depth {} root {}'.format(current_depth,root.data))
                depth = max(current_depth,depth)
                if root.left:
                  stack.append((current_depth+1,root.left))
                if root.right:
                  stack.append((current_depth+1,root.right))
            return depth
            
        
    
b = BinarySearchTree()
root=None
for ele in [2,1,33,0,25,40,11,34,7,12,36,13]:
    root=b.buildBinarySearchTree(root,ele)

totalNodes=b.countTotalNodes(root)
print("Total no of nodes in the given Binary tree are {}".format(totalNodes))

leafNodes = b.countLeafNodes(root)
print("Total Leaf Nodes {}".format(leafNodes))
        

maxDepthRecursive = b.maxDepthOfTree(root)
print(maxDepthRecursive)
maxDepthIterative = b.maxDepthIterativeApproach(root)
print(maxDepthIterative)
