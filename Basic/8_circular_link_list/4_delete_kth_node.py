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

def delete_head_efficient(head):
    if head == None:
        return None
    if head.next == head:
        return None
    head.data = head.next.data
    head.next  = head.next.next
    return head

def delete_kth_node(head,k):
    if head == None:
        return head
    if k == 1:
        return delete_head_efficient(head)
    curr = head
    for _ in range(k-2):
        curr = curr.next
    curr.next = curr.next.next
    return head





head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)
node5 = Node(60)
node6 = Node(70)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = head


traverse(head)
head = delete_kth_node(head,2)
traverse(head)