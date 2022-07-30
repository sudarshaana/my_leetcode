class Bucket:
    def __init__(self):
        #self.list = []
        self.head = Node(0) # pseudo Head
        
    def add(self, key):
        if not self.contains(key):
            #self.list.append(key)
            self.head.next = Node(key, self.head.next)
            
        
    def remove(self, key):
        # for i in self.list:
        #     if i == key:
        #         self.list.remove(i)
        #         break
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.val == key:
                prev.next = current.next
                return
            prev = current
            current = current.next
            
    def contains(self, key):
        # for i in self.list:
        #     if i == key:
        #         return True
        # return False
        current = self.head.next
        while current is not None:
            if current.val == key:
                return True
            current = current.next
        return False
    
class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node
    
class MyHashSet:

    def __init__(self):
        self.key = 769
        self.buckets = [Bucket() for i in range(self.key)]
        

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