class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.prev = None
        self.next = None

def insert_begin(head,x):
    temp = Node(x)
    temp.next = head
    if head != None:
        head.prev = temp
    return temp

def traverse(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
    
def reverse(head):
    if head is None or head.next is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        prev = curr.prev
        curr.prev, curr.next = curr.next, curr.prev
        curr = curr.prev
    return prev.prev
        



head = None
head = insert_begin(head,50)
head = insert_begin(head,40)
head = insert_begin(head,30)
head = insert_begin(head,20)
head = insert_begin(head,10)
traverse(head)
head = reverse(head)
traverse(head)