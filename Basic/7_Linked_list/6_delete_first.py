class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

def delete_first(head):
    if head == None:
        return None
    else:
        temp = head.next
        head = None # Not  necessary, python garbage collector clean up unreferenced npdes
        return temp



head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3
show(head)
head = delete_first(head)
show(head)
