class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

def reverse_naive(head):
    val = []
    curr = head
    while curr:
        val.append(curr.data)
        curr = curr.next
    curr = head
    while curr:
        temp = val.pop()
        curr.data = temp
        curr = curr.next
    return head

def reverse_efficient(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def recursive_1(head):
    if not head or not head.next:
        return head
    rest_head = recursive_1(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head

def recursive_2(head,prev=None):
    if not head:
        return prev
    next = head.next
    head.next = prev
    return recursive_2(next,head)

def reverse_swap(head):
    p = q = head
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    
    i = 0
    j = length-1

    while i<j:
        k = 0
        while(k<j):
            q = q.next
            k += 1
        q.data, p.data = p.data, q.data
        i += 1
        j -= 1
        p = p.next
        q = head
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

show(head)
head = reverse_swap(head)
show(head)