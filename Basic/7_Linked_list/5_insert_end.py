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
def insert_end_iterative(head,key):
    temp = Node(key)
    if head == None:
        return temp
    curr = head
    while(curr.next):
        curr = curr.next
    curr.next = temp
    return head




#head = None
head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3
show_recursive(head)
head = insert_end_iterative(head,50)
show_recursive(head)