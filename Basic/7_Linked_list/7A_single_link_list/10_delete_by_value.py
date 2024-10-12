class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def show(head):
    curr = head
    while(curr):
        print(curr.data)
        curr = curr.next

def delete_value(head, key):
    if head == None:
        return None
    
    if head.data == key:
        return head.next
    
    curr = head
    while curr.next:
        if curr.next.data == key:
            curr.next = curr.next.next
            return head
        curr = curr.next

    print('not found')
    return head
        
        


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3
show(head)
head = delete_value(head,50)
print('after removing')
show(head)








