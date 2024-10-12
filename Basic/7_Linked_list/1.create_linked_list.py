class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
node1 = Node(20)
node2 = Node(30)

head.next = node1
node1.next = node2

