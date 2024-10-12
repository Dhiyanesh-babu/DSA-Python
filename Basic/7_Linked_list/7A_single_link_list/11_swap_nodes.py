class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next


def swap_ref(head,pos1,pos2): 
    if pos1 == pos2:
        return head
    prev1 = prev2 = None
    curr1 = curr2 = head
    for _ in range(pos1-1):
        prev1 = curr1
        curr1 = curr1.next
    for _ in range(pos2-1):
        prev2 = curr2
        curr2 = curr2.next
    if not curr1 or not curr2:
        return head
    if prev1:
        prev1.next = curr2
    else:
        head = curr2
    if prev2:
        prev2.next = curr1
    else:
        head = curr1
    curr1.next, curr2.next = curr2.next, curr1.next

    return head


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

show(head)
head = swap_ref(head,5,4)
print('after swapping')
show(head)




