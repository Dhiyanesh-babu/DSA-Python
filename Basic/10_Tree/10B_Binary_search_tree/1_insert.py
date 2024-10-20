from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def levelorder(root):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        size = len(q)
        for i in range(size):
            temp = q.popleft()
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            print(temp.val, end = '\t')


def insert_iterative(root,x):
    temp = Node(x)
    curr = root
    while curr:
        parent = curr
        if curr.val > x:
            curr = curr.left
        elif curr.val < x:
            curr = curr.right
        else:
            return root
    if parent == None:
        return temp
    elif parent.val > x:
        parent.left = temp
    else:
        parent.right = temp
    return root

def recursive_insert(root,x):
    if not root:
        return Node(x)
    elif root.val < x:
        root.right = recursive_insert(root.right,x)
    elif root.val > x:
        root.left = recursive_insert(root.left,x)
    return root
    






root = Node(15)
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.right.left = Node(18)
root.right.right = Node(80)

root.right.left.left = Node(16)

levelorder(root)
print('\n')
#root = recursive_insert(root,7)
root = recursive_insert(root,7)
levelorder(root)




# recursive time and space - O(h)
# iterative time O(h) and space 0





















