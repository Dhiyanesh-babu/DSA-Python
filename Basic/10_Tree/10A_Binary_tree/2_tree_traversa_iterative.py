from collections import deque


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
   stack = deque()
   curr = root
   while curr or stack:
        while curr:
           stack.append(curr)
           curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right
# Time O(N) Space O(h)
        



def preorder(root):
    st = deque()
    if not root:
        return
    st.append(root)
    while st:
        curr = st.pop()
        print(curr.val)
        if curr.right:
            st.append(curr.right)
        if curr.left:
            st.append(curr.left)
    
def space_efficient_preorder(root):
    st = deque()
    curr = root
    while curr or st:
        while curr:
            print(curr.val)
            if curr.right:
                st.append(curr.right)
            curr = curr.left
        if st:
            curr = st.pop()


def postorder_2stack(root):
    if root == None:
        return
    s1 = deque()
    s2 = deque()
    s1.append(root)

    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        node = s2.pop()
        print(node.val)


def postorder_1stack(root):
    stack = []
    curr = root
    while curr is not None or len(stack) > 0:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if temp is None:
                temp = stack.pop()
                print(temp.val)
                while len(stack) > 0 and temp == stack[-1].right:
                    temp = stack.pop()
                    print(temp.val)
            else:
                curr = temp
     



    
    

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right.right = Node (60)
print('inoder:')
inorder(root)
print('preorder:')
preorder(root)
print('space_efficient_preorder')
space_efficient_preorder(root)
print('postorder 2 stack:')
postorder_2stack(root)
print('postorder 1 stack:')
postorder_1stack(root)










