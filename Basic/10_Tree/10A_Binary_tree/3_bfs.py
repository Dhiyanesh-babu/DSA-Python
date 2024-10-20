from collections import deque


# Time O(2N)
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    else:
        return max(height(root.left), height(root.right))+1
    
def printlevel(root,level):
    if root == None:
        return
    elif level == 0:
        print(root.val)
    else:
        printlevel(root.left,level-1)
        printlevel(root.right,level-1)

def bfs(root):
    h = height(root)
    for i in range(h):
        printlevel(root,i)


def bfs_iterative(root):
    if root is None:
        return
    
    q = deque([root])
    
    while q:
        size = len(q)
        for _ in range(size):
            temp = q.popleft()   
            print(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)



root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node (60)
bfs(root)
print('new')
bfs_iterative(root)