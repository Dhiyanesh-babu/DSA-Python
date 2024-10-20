from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None



def search_recursive(root,x):
    if root == None:
        return False
    if root.val == x:
        return True
    elif root.val > x:
        return search_recursive(root.left,x)
    else:
        return search_recursive(root.right,x)

    
def search_iterative(root,x):
    curr = root
    while curr:
        if curr.val == x:
            return True
        elif curr.val > x:
            curr = curr.left
        else:
            curr = curr.right
    return False


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



root = Node(15)
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.right.left = Node(18)
root.right.right = Node(80)

root.right.left.left = Node(16)

levelorder(root)
print('\n')
ans = search_recursive(root,16)
print(ans)
print('\n')
ans = search_iterative(root,16)
print(ans)



# recursive time and space - O(h)
# iterative time O(h) and space 0
