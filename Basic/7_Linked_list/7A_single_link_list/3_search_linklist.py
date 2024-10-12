class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def search_iterative(head, key):
    while(head):
        if head.data == key:
            print('found')
            return
        head = head.next
    print('not found')

def search_recursive(head, key):
    if head == None:
        print('not found')
        return-1
    if (head.data == key):
        print('found')
        return 1
    else:
        res = search_recursive(head.next,key)
        if res == -1:
            return -1
        else:
            return (res+1)

    


head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)

head.next = node1
node1.next = node2
node2.next = node3


ans = search_recursive(head, 40)
print(ans)