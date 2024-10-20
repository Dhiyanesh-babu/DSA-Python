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

# nearest greater number will be always left most node on right side
def successor(root):
    curr = root.right
    while curr and curr.left:
        curr = curr.left
    return curr

def delete(root,x):
    if not root:
        return root
    elif root.val > x:
        root.left = delete(root.left,x)
    elif root.val < x:
        root.right = delete(root.right,x)
    else:
        if not root.left:
            temp = root.right
            return temp
        elif not root.right:
            temp = root.left
            return temp
        else:
            succ = successor(root)
            root.val = succ.val
            root.right = delete(root.right, succ.val)

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
root = delete(root,20)
levelorder(root)