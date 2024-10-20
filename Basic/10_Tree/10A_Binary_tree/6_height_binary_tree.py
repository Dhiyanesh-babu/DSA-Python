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






root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node (60) 

ans = height(root)
print(ans)





