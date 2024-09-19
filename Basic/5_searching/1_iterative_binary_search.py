class  binary_search:
    def __init__(self,arr,x) -> None:
        self.arr = arr
        self.x = x
    def find(self):
        low = 0
        high =  len(self.arr)-1
        while(low<=high):
            mid = (low+high)//2
            if self.arr[mid] == self.x:
                return mid
            if self.arr[mid] > x:
                high = mid-1
            else:
                low = mid+1
        return -1


sample = [10,20,30,40,50,60,70]
x = 300
obj = binary_search(sample,x)
ans = obj.find()
print(ans)

# Time O(logN)