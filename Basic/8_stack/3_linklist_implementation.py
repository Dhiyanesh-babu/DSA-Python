class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def push(head,x):
    temp = Node(x)
    temp.next = head
    head = temp
    return head

def pop(head):
    if head == None:
        return 
    res = head.data
    print('popped',res)
    head = head.next
    return head


def traverse(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next




head = None

head = push(head, 10)
head = push(head, 20)
head = push(head, 30)
head = push(head, 40)
head = push(head, 50)


head = pop(head)
head = pop(head)


traverse(head)
    

