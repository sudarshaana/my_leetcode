class Bucket:
    def __init__(self):
        self.list = []
        
    def add(self, key):
        if not self.contains(key):
            self.list.append(key)
        
    def remove(self, key):
        for i in self.list:
            if i == key:
                self.list.remove(i)
                break
            
    def contains(self, key):
        for i in self.list:
            if i == key:
                return True
        return False
    
class MyHashSet:

    def __init__(self):
        self.key = 7919
        self.buckets = [Bucket()]*self.key
        

    def add(self, key: int) -> None:
        hash_key = key%self.key
        self.buckets[hash_key].add(key)
        

    def remove(self, key: int) -> None:
        hash_key = key%self.key
        self.buckets[hash_key].remove(key)
        

    def contains(self, key: int) -> bool:
        hash_key = key%self.key
        return self.buckets[hash_key].contains(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)