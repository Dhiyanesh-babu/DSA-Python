class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class binary_tree_size:
    def __init__(self,root) -> None:
        self.root = root

    def find_size(self,root):
        if root == None:
            return 0
        else:
            return 1 + self.find_size(root.left) + self.find_size(root.right)
        


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node (60) 

obj = binary_tree_size(root)
ans = obj.find_size(root)
print(ans)



