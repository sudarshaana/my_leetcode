class MyHashMap:
    
    def __init__(self):
        self.data = []
        

    def put(self, key: int, value: int) -> None:
        for i, d in enumerate(self.data):
            if d[0] == key:
                self.data[i] = [key, value]
                return
        
        self.data.append([key, value])
        

    def get(self, key: int) -> int:
        for d in self.data:
            if d[0] == key:
                return d[1]
        return -1

    def remove(self, key: int) -> None:
        for d in self.data:
            if d[0] == key:
                self.data.remove(d)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)