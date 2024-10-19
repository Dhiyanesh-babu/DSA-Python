from collections import deque

class CustomDeque:
    def __init__(self):
        """Initialize an empty deque."""
        self.deque = deque()

    def append(self, value):
        """Add an element to the right end of the deque."""
        self.deque.append(value)
        print(f'Added to right: {value}')

    def appendleft(self, value):
        """Add an element to the left end of the deque."""
        self.deque.appendleft(value)
        print(f'Added to left: {value}')

    def pop(self):
        """Remove and return the rightmost element from the deque."""
        if self.deque:
            value = self.deque.pop()
            print(f'Removed from right: {value}')
            return value
        print('Deque is empty, cannot pop from right.')
        return None

    def popleft(self):
        """Remove and return the leftmost element from the deque."""
        if self.deque:
            value = self.deque.popleft()
            print(f'Removed from left: {value}')
            return value
        print('Deque is empty, cannot pop from left.')
        return None

    def extend(self, iterable):
        """Add multiple elements to the right end of the deque."""
        self.deque.extend(iterable)
        print(f'Extended right with: {list(iterable)}')

    def extendleft(self, iterable):
        """Add multiple elements to the left end of the deque."""
        self.deque.extendleft(iterable)
        print(f'Extended left with: {list(iterable)}')

    def rotate(self, n):
        """Rotate the deque n steps to the right (if n is positive) or left (if negative)."""
        self.deque.rotate(n)
        direction = 'right' if n > 0 else 'left'
        print(f'Rotated {abs(n)} steps to the {direction}.')

    def count(self, value):
        """Count occurrences of a specified value in the deque."""
        count_value = self.deque.count(value)
        print(f'Count of "{value}": {count_value}')
        return count_value

    def clear(self):
        """Remove all elements from the deque."""
        self.deque.clear()
        print('Cleared the deque.')

    def display(self):
        """Display the current state of the deque."""
        print(f'Current deque: {self.deque}')


# Example usage of the CustomDeque class
if __name__ == "__main__":
    my_deque = CustomDeque()

    my_deque.append('a')
    my_deque.append('b')
    my_deque.appendleft('c')
    my_deque.appendleft('d')
    
    my_deque.display()

    my_deque.pop()
    my_deque.popleft()

    my_deque.display()

    my_deque.extend(['e', 'f', 'g'])
    my_deque.extendleft(['h', 'i'])

    my_deque.display()

    my_deque.rotate(2)
    my_deque.rotate(-1)

    my_deque.count('e')
    my_deque.clear()

    my_deque.display()

