'''
Here I am trying to create a binary tree such that whatever value comes
goes to left and if there is some value stored in left then only it will
store it to the right.

1,2,3,4,5,6
        1
      /   \
    2      3
   / \    / \
  4   5   6
'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
class Tree(Node):
    def insert(self,node):
        root=self
        if root==None:
            root = node
        else:
            if root.left==None and root.right==None:
                root.left= node
            elif root.left!=None:
                root.right = node
                
    def print_tree(self):
        root= self
        if root==None:
            return
        temp = []
        flag=1
        while flag:
            if root!=None:
                temp.append(root)
                root = root.left
            else:
                if temp:
                    root = temp.pop()
                    print(root.val, end=" ")
                    root = root.right
                else:
                    flag=0
                
n1 = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5)
n6 = Tree(6)
n7 = Tree(7)

n1.insert(n2)
n1.insert(n3)
n2.insert(n4)
n2.insert(n5)
n3.insert(n6)
n5.insert(n7)

n1.print_tree()
