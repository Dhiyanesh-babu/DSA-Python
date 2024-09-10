class mergesort_array:
    def merge(self,arr,l,m,r):
        n1,n2 = m-l+1, r-m
        left, right = [],[]
        for i in range(n1):
            left.append(arr[l+i])
        for i in range(n2):
            right.append(arr[m+i+1])
        i,j = 0,0
        k = l
        while(i<n1 and j<n2):
            if left[i] <= right[j]:
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1
        while(i<n1):
            arr[k] = left[i]
            k += 1
            i += 1
        while(j<n2):
            arr[k] = right[j]
            k += 1
            j += 1
    def merge_sort(self,arr, l, r):
        if (r>l):
            m = (l + (r-l)//2)
            mergesort_array.merge_sort(self,arr,l,m)
            mergesort_array.merge_sort(self,arr,m+1,r)
            mergesort_array.merge(self,arr,l,m,r)
        
    
sample = [10,5,30,15,7]
length = len(sample)
obj = mergesort_array()
obj.merge_sort(sample,0,length-1)
print(sample)







        