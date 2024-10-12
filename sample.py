class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def show(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

def swap_ref(head, pos1, pos2):
    if pos1 == pos2:
        return head
    
    # Find nodes before pos1 and pos2 and the corresponding nodes
    prev1 = prev2 = None
    curr1 = curr2 = head
    
    # Locate node at pos1
    for _ in range(pos1 - 1):
        prev1 = curr1
        curr1 = curr1.next
    
    # Locate node at pos2
    for _ in range(pos2 - 1):
        prev2 = curr2
        curr2 = curr2.next
    
    # If either node is not found, do nothing
    if not curr1 or not curr2:
        return head

    # Swap the nodes by changing references
    if prev1:
        prev1.next = curr2
    else:
        head = curr2  # If curr1 is head, make curr2 the new head

    if prev2:
        prev2.next = curr1
    else:
        head = curr1  # If curr2 is head, make curr1 the new head

    # Swap the next pointers of curr1 and curr2
    curr1.next, curr2.next = curr2.next, curr1.next

    return head

# Creating a linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
node1 = Node(20)
node2 = Node(30)
node3 = Node(40)
node4 = Node(50)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
show(head)

# Swap nodes at positions 3 and 4 (nodes 30 and 40)
head = swap_ref(head, 3, 4)

print("List after swapping nodes at positions 3 and 4:")
show(head)
