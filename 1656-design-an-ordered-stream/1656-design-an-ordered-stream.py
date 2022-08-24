class OrderedStream:

    def __init__(self, n: int):
        self.d = [None]*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.d[idKey-1] = value
        
        res = []
        for item in self.d[self.ptr:]:
            if item == None:
                break
            else:
                res.append(item)
                self.ptr+=1
            
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)