class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def array2bst(num):
    l = len(num)
    if l==0:
        return None
    if l==1:
        return Node(num[0])
    root = Node(num[l//2])
    root.left = array2bst(num[:l//2])
    root.right = array2bst(num[1//2+1:])
    return root

def tree(cur):
    if cur==None:
        return
    tree(cur.left)
    print(cur.val, end =" ")
    tree(cur.right)
        
cur =array2bst([1,2,3,4,5])
print(cur.val)
tree(cur)
