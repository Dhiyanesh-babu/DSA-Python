
class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None


def traverse(head):
    curr = head
    while True:
        print(curr.data)
        curr = curr.next
        if curr == head:
            break

def insert_end_naive(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return head

def insert_end_efficient(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    temp.next = head.next
    head.next = temp
    temp.data, head.data = head.data, temp.data
    return temp  

head = Node(10)
node1 = Node(20)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = head


traverse(head)
head = insert_end_efficient(head,90)
traverse(head)
