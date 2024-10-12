class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

def insert_pos(head, key, pos):
    temp = Node(key)
    curr = head

    if pos == 1:
        temp.next = head
        return temp
    
    for _ in range(pos-2):
        curr = curr.next
        if not curr:
            print('index out of range')
            return head
    temp.next = curr.next
    curr.next = temp
    return head
 


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3
show(head)
head = insert_pos(head,25,1)
show(head)
