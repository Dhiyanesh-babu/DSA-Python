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
    
def delete_last(head):
    if head is None or head.next is None:
        return head
    curr = head
    while curr.next:
        curr = curr.next
    curr.prev.next = None
    return head



head = None
head = insert_begin(head,50)
head = insert_begin(head,40)
head = insert_begin(head,30)
head = insert_begin(head,20)
head = insert_begin(head,10)
traverse(head)
head = delete_last(head)
traverse(head)