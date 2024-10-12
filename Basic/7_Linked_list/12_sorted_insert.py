class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
    
def show(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def sorted_insert(head,key):
    prev = curr = head
    temp = Node(key)
    if key < head.data:
        temp.next = head
        return temp
    while curr:
        if curr.next is None or curr.next.data > key:
                temp.next = curr.next
                curr.next = temp
                return head
        curr = curr.next



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
head = sorted_insert(head,55)
print('after swapping')
show(head)

