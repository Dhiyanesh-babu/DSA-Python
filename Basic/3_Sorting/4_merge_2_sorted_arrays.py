class merge_sorted_array:
    def __init__(self, data1, data2) -> None:
        self.arr1 = data1 
        self.arr2 =  data2
    def merge(self):
        n = len(self.arr1)
        i,j = 0,0
        while(i<n and j<n):
            if(self.arr1[i] < self. arr2[j]):
                print(self.arr1[i])
                i +=1
            else:
                print(self.arr2[j])
                j +=1
        while(i<n):
            print(arr1[i])
            i += 1
        while(j<n):
            print(arr2[j])
            j +=1
# Time O(m+n)

        
arr1 = (10,15,20,40)
arr2 = (5,6,6,10,15)
obj =  merge_sorted_array(arr1, arr2)
ans = obj.merge()
