class chain_hash:
    def __init__(self, b) -> None:
        self.bucket = b
        self.table = [set() for _ in range(b)]

    def hash(self, key):
        return key%self.bucket
    
    def insert(self, key):
        index = self.hash(key)
        self.table[index].add(key)
        
    def search(self,key):
        index = self.hash(key)
        for a in self.table[index]:
            if a == key:
                return True
        return False
    
    def delete(self, key):
        index = self.hash(key)
        self.table[index].discard(key)

    def show(self):
        print(self.table)

    def load_factor(self):
        return sum(len(bucket) for bucket in self.table) / self.bucket

    def resize(self):
        new_bucket = self.bucket * 2
        new_table = [set() for _ in range(new_bucket)]
        for bucket in self.table:
            for key in bucket:
                new_index = key % new_bucket
                new_table[new_index].add(key)
        self.bucket = new_bucket
        self.table = new_table
        
    def __iter__(self):
        for bucket in self.table:
            for key in bucket:
                yield key


obj = chain_hash(7)
obj.insert(51)
obj.insert(65)
obj.insert(72)
obj.show()
obj.delete(65)
obj.show()
obj.insert(52)
obj.resize()
obj.show()

for key in obj:
    print(key)







