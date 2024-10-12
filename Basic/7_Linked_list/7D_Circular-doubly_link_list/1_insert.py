class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.prev = None
        self.next = None

def traverse(head):
    if not head:
        return
    curr = head
    while True:
        print(curr.data)
        curr = curr.next
        if curr == head:
            break

 
def insert_begin(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        temp.prev = temp
        return temp
    temp.prev = head.prev
    head.prev.next = temp
    temp.next = head
    head.prev = temp

    return temp

def insert_last(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        temp.prev = temp
        return temp
    temp.prev = head.prev
    head.prev.next = temp
    temp.next = head
    head.prev = temp

    return head

   
   
head = None
head = insert_last(head,50)
head = insert_last(head,40)
head = insert_last(head,30)
head = insert_last(head,20)
head = insert_last(head,10)
traverse(head)