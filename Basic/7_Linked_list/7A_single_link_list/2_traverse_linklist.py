class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def show_iterative(head):
    current = head
    while(current):
        print(current.data)
        current = current.next

def show_recursive(head):
    if not head:
        return 
    print(head.data)
    show_recursive(head.next)


head = Node(10)
node1 = Node(20)
node2 = Node(30)

head.next = node1
node1.next = node2

#show_iterative(head)
show_recursive(head)