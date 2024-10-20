class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def maximum_binary_tree(root):
    if root == None:
        return float('-inf')
    else:
        return max(root.val,maximum_binary_tree(root.left),maximum_binary_tree(root.right))
    



root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node (60) 

ans = maximum_binary_tree(root)
print(ans)
