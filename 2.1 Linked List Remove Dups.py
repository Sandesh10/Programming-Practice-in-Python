class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def remove_duplicate(self):
        node = self
        while node!=None:
            temp = node
            while temp.next!=None:
                if temp.next.data == node.data:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            node = node.next 

    def traversal(self):
        node= self
        while node !=None:
            print(node.data, end ="-->")
            node = node.next

def main():
    node1 = Node(22)
    node2 = Node(2)
    node3 = Node(2)
    node4 = Node(33)
    node5 = Node(22)
    node6 = Node(21)
    node7 = Node(22)
        
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
        
    node1.remove_duplicate()
    node1.traversal()    
if __name__=='__main__':
    main()
