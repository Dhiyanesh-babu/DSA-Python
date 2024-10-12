class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


def mid_naive(head):
    curr = head
    count = 0
    if head == None:
        return None
    while curr:
        count += 1
        curr = curr.next
    curr = head
    for _ in range(count//2):
        curr  = curr.next
    print(curr.data)
    return head

def mid_optimised(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)
    return head


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


head = mid_naive(head)
head = mid_optimised(head)



