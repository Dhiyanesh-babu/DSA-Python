class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

def delete_pos(head, pos):
    if pos == 1:
        return head.next
    p = head
    i = 1
    while (i<pos-1):
        if p.next is None:
            print('index out of range')
            return head
        p = p.next
        i += 1
        
    if p.next is None:
        print('index out of range')
        return head

    q = p.next
    p.next = q.next
    return head


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3
show(head)
head = delete_pos(head,5)
print('after removing')
show(head)





