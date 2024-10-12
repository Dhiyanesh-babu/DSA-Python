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

def delete_head_naive(head):
    if head == None:
        return None
    if head.next == head:
        return None
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = curr.next.next
    return curr.next

def delete_head_efficient(head):
    if head == None:
        return None
    if head.next == head:
        return None
    head.data = head.next.data
    head.next  = head.next.next
    return head

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
head = delete_head_efficient(head)
traverse(head)