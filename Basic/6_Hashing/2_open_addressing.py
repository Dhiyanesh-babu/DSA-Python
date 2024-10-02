class open_addressing_hash:
    def __init__(self, c) -> None:
        self.cap = c
        self.size = 0
        self.arr = [-1]*self.cap 

    def hash(self, key):
        return key % self.cap
    
    def insert(self, key):
        if self.size == self.cap:
            return False
        h = self.hash(key)
        i = h
        while(self.arr[i] not in (-1,-2,key)):
            i = (i+1) % self.cap
            if i == h:
                return False
        if self.arr[i] == key:
            return False
        else:
            self.arr[i] = key
            self.size += 1
            print('insertes',key)
            return True
        
    def erase(self, key):
        h = self.hash(key)
        i = h
        while(self.arr[i] != -1):
            if self.arr[i] == key:
                self.arr[i] = -2
                self.size -= 1
                return True
            i = (i+1) % self.cap
            if i == h:
                return False
        return False 
    
    def search(self, key):
        h = self.hash(key)
        i = h
        while(self.arr[i] != -1):
            if self.arr[i] == key:
                return True
            i = (i+1) % self.cap
            if i == h:
                return False
        return False
    def show(self):
        print(self.arr)
    

obj = open_addressing_hash(7)
obj.insert(49)
obj.insert(55)
obj.insert(72)
obj.insert(56)
obj.insert(52)
obj.insert(53)
obj.insert(54)
obj.erase(52)
obj.insert(90)
obj.show()



             
    

