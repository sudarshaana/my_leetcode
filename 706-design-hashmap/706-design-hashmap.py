class Bucket:
    def __init__(self):
        self.bucket = []
        
    def update(self, key, val):
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                self.bucket[i] = (key, val)
                found = True
            if found:
                break
        if not found:
            self.bucket.append((key, val))
            
    def get(self, key):
        for k,v in self.bucket:
            if k == key:
                return v
        return -1
                
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]
                
        

class MyHashMap:
    
    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]
        

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space 
        return self.hash_table[hash_key].get(key)


    def remove(self, key: int) -> None:        
        hash_key = key % self.key_space 
        self.hash_table[hash_key].remove(key)
                

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)