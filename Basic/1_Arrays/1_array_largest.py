class largest:
    def __init__(self,numbers) -> None:
        self.numbers =  numbers
    def biggest(self) -> int:
        if not self.numbers:
            return None
        else:
            return max(self.numbers)


sample = [1,2,3,9,8,7,11,2,5,6,7]
obj = largest(sample)
ans = obj.biggest()
print(ans)


# Time - O(N)
# Space - O(1)










# optimised

class Largest:
    def __init__(self, numbers) -> None:
        self.numbers = numbers

    def biggest(self) -> int:
        return max(self.numbers, default=None) # O(N)

sample = [1, 2, 3, 9, 8, 7, 11, 2, 5, 6, 7]
obj = Largest(sample)
ans = obj.biggest()
print(ans)


"""
In the provided code, when you initialize the Largest object with obj = Largest(sample), the self.numbers attribute of the object refers to the same list that is passed as the sample. 
No extra copy of the array is created; instead, the object holds a reference to the original list.

Therefore, any changes made to the sample list outside of the Largest class will be reflected in the self.numbers attribute of the obj object. 
This behavior is due to the fact that lists in Python are mutable, and when you pass a mutable object like a list to a function or store it in an attribute, you are working with a reference to the same object, not a copy.

"""