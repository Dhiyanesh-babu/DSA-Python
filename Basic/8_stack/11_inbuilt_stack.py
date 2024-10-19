# using deque for stack is more efficient

from collections import deque

class Stack:
    def __init__(self):
        # Initialize an empty deque for the stack
        self.stack = deque()

    def push(self, element):
        self.stack.append(element)
        print(f"Pushed {element} to stack")

    def pop(self):
        if not self.is_empty():
            popped_element = self.stack.pop()
            print(f"Popped {popped_element} from stack")
            return popped_element
        else:
            print("Stack is empty. No element to pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty."

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage:
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
print(my_stack.peek())  # Output: 20
my_stack.pop()  # Removes 20
my_stack.pop()  # Removes 10
my_stack.pop()  # Stack is empty




# class Stack:
#     def __init__(self):
#         # Initialize an empty list for the stack
#         self.stack = []

#     # Push an element to the stack
#     def push(self, element):
#         self.stack.append(element)
#         print(f"Pushed {element} to stack")

#     # Pop an element from the stack
#     def pop(self):
#         if not self.is_empty():
#             popped_element = self.stack.pop()
#             print(f"Popped {popped_element} from stack")
#             return popped_element
#         else:
#             print("Stack is empty. No element to pop.")
#             return None

#     # Peek at the top element of the stack
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             return "Stack is empty."

#     # Check if the stack is empty
#     def is_empty(self):
#         return len(self.stack) == 0

#     # Get the size of the stack
#     def size(self):
#         return len(self.stack)

# # Example usage:
# my_stack = Stack()
# my_stack.push(10)
# my_stack.push(20)
# print(my_stack.peek())  # Output: 20
# my_stack.pop()  # Removes 20
# my_stack.pop()  # Removes 10
# my_stack.pop()  # Stack is empty
