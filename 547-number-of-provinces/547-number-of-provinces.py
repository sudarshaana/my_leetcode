class City:
    
    def __init__(self, size):
        self.root =  [i for i in range(size)]
        self.rank = [1]*size
    
    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    
    def union(self, x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX]+=1
                
                
    def isConected(self, x,y):
        return self.root[x] == self.root[y]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        city_count = len(isConnected)
        uf = City(city_count)

        for index, city in enumerate(isConnected):

            for i, link in enumerate(city):
                if i!=index:
                    if link!=0:
                        uf.union(index, i)


        p = set()
        for city in range(city_count):

            p.add(uf.find(city))

        return(len(p))
        