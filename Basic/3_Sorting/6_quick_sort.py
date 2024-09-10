class quick_sort_array:
    def lometo_partition(self,arr,l,h):
        pivot = arr[h]
        index = l-1
        for j in range(l,h):
            if arr[j] < pivot:
                index += 1
                arr[index], arr[j] = arr[j], arr[index]
        arr[index+1], arr[h] = arr[h], arr[index+1]
        return index+1
    def hoares_partiion(self,arr,l,h):
        i = l
        j = h
        pivot = arr[l]
        while True:
            while arr[i]<pivot:
                i += 1
            while arr[j]>pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]
        

    def quick_sort(self,arr, l, h):
        if(l<h):
            p = quick_sort_array.hoares_partiion(self,arr,l,h)
            quick_sort_array.quick_sort(self,arr,l,p-1)
            quick_sort_array.quick_sort(self,arr,p+1,h)
            

sample = [5,3,8,4,2,7,1,10]
length = len(sample)
obj = quick_sort_array()
obj.quick_sort(sample,0,length-1)
print(sample)