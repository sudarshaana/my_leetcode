from random import randint

class RandomizedSet:

    def __init__(self):
        self.d = set()

    def insert(self, val: int) -> bool:
        exists = True if val in self.d else False
        self.d.add(val)
        return not exists

    def remove(self, val: int) -> bool:
        exists = True if val in self.d else False
        if exists:
            self.d.remove(val)
        return exists

    def getRandom(self) -> int:
        
        l = len(self.d)
        i = 0
        r_v = randint(0, l-1)
        
        for v in self.d:
            if i == r_v:
                return v
            i+=1


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()