class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def n_from_last(head, n):
    first = head
    second = head
    for _ in range(n-1):
        if first.next is None:
            print("n is greater than linklist")
            return
        first = first.next

    while first.next:
        first = first.next
        second = second.next
    print(second.data)



head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

n_from_last(head,9)