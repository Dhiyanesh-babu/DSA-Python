
class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None


def insert_begin_naive(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
    else:
        curr = head
        while curr.next != head:
            curr = curr.next
        curr.next = temp
        temp.next = head
    return temp

def insert_begin_efficient(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:  
        temp.next = head.next
        head.next = temp
        head.data, temp.data = temp.data, head.data
        return head

def traverse(head):
    curr = head
    while True:
        print(curr.data)
        curr = curr.next
        if curr == head:
            break


head = None 
head = insert_begin_efficient(head, 10)
head = insert_begin_efficient(head, 20)
head = insert_begin_efficient(head, 30)
traverse(head)


