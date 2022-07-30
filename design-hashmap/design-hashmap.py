class Bucket:
    def __init__(self):
        self.list = []
        
    def put(self, key, value):
        found = False
        for i, item in enumerate(self.list):
            if item[0] == key:
                found  = True
                self.list[i] = [key, value]
                break
        if not found:
            self.list.append([key, value])
            
        
    def remove(self, key):
        for i in self.list:
            if i[0] == key:
                self.list.remove(i)
                break
            
    def get(self, key):
        for i in self.list:
            if i[0] == key:
                return i[1]
        return -1
    
    
class MyHashMap:

    def __init__(self):
        self.key = 1993
        self.buckets = [Bucket() for i in range(self.key)]
        

    def put(self, key: int, value: int) -> None:
        hash_key = key%self.key
        self.buckets[hash_key].put(key, value)
        

    def remove(self, key: int) -> None:
        hash_key = key%self.key
        self.buckets[hash_key].remove(key)
        

    def get(self, key: int) -> bool:
        hash_key = key%self.key
        return self.buckets[hash_key].get(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)