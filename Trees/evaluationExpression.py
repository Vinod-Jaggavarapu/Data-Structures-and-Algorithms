class Node:
  def __init__(self,data,left=None,right=None):
    self.data = data
    self.left=None
    self.right =None


def evaluateExpression(root):
  if root.left==None and root.right==None:
    return root.data
  else:
    left = evaluateExpression(root.left)
    right = evaluateExpression(root.right)
    return eval(str(left)+root.data+str(right))


            


root = Node('*')
root.left = Node('+')
root.right = Node('*')
root.left.left = Node(2)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node('+')
root.right.right.left = Node(5)
root.right.right.right = Node(6)

print(evaluateExpression(root))
