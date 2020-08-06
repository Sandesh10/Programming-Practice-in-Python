class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
class Tree(Node):
    def insert(self,node):
        root = self
        if not root:
            return None
        if not root.left and not root.right:
            root.left = node
        elif root.left:
            root.right = node
            
    def print_tree(self, root):
        if not root:
            return 
        print(root.val)
        self.print_tree(root.left)
        self.print_tree(root.right)
        
    def max_path(self,root):
        rightpath = []
        leftpath = []
        if not root:
            return None
        if not root.left and not root.right:
            return [root.val]
        if root.right is not None:
            rightpath =  [root.val] + self.max_path(root.right)
            #print("rightpath",rightpath)
        if root.left is not None:
            leftpath = [root.val] + self.max_path(root.left)
            #print("leftpath", leftpath)
        return (rightpath if len(rightpath)> len(leftpath) else leftpath)
    
    
n1 = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5)
n6 = Tree(6)
n7 = Tree(7)
n8 = Tree(8)
n9 = Tree(9)
n1.insert(n2)
n1.insert(n3)
n2.insert(n4)
n4.insert(n5)
n4.insert(n6)
n3.insert(n7)
n3.insert(n8)
n8.insert(n9)
n9.insert(Tree(10))
# n1.print_tree(n1)
print(n1.max_path(n1))
