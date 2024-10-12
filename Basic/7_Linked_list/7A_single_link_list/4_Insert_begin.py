class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def show_recursive(head):
    if not head:
        return 
    print(head.data)
    show_recursive(head.next)

# by returning head
def insert_begin(head,key):
    temp = Node(key)
    temp.next = head
    return temp

# by changig global head
def insert_begin_global(key):
    global head  
    temp = Node(key)
    temp.next = head
    head = temp 


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3
show_recursive(head)
insert_begin_global(5)
show_recursive(head)