class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.prev = None
        self.next = None

def insert_end(head,x):
    temp = Node(x)
    if head == None:
        return temp
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head


def traverse(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next
    
head = None
head = insert_end(head,50)
head = insert_end(head,40)
head = insert_end(head,30)
head = insert_end(head,20)
head = insert_end(head,10)
traverse(head)
