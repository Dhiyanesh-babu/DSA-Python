class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head




head = Node(10)
node1 = Node(20)
node2 = Node(20)
node3 = Node(30)
node4 = Node(30)
node5 = Node(30)
node6 = Node(30)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


show(head)
head = remove_duplicates(head)
show(head)