class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

def delete_last(head):
    if head == None or head.next is None :
        return None
    else:
        curr = head
        while(curr.next.next):
            curr = curr.next
        curr.next = None

    return head
        


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3
show(head)
head = delete_last(head)
show(head)
