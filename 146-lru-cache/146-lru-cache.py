class LRUCache:

    def __init__(self, capacity: int):
        self.capacity= capacity
        self.size = 0
        self.access_list = []
        self.cache = {}
        

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.access_list.remove(key)
            self.access_list.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache[key] = value
            
            self.access_list.remove(key)
            self.access_list.append(key)
            
        else:
            self.cache[key] = value
            #print("adding {}:{}".format(key, value))
            # add to cache
            self.size+=1
        
            # removing lru if full
            self.access_list.append(key)
            if len(self.access_list) > self.capacity:
                hash_key = self.access_list.pop(0)
                del self.cache[hash_key]
                self.size -= 1
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)