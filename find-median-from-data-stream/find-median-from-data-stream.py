from bisect import bisect

class MedianFinder:

    def __init__(self):
        self.list = []
        self.count = 0
        
    def addNum(self, num: int) -> None:
        insert_pos = bisect(self.list, num)
        self.list.insert(insert_pos, num)
        self.count += 1

    def findMedian(self) -> float:
        if self.count == 0:
            return 
        
        if self.count % 2 != 0:
            return self.list[(self.count//2)]
        
        return (self.list[(self.count // 2) - 1] + self.list[(self.count // 2)] )/2

        

#     def addNum(self, num: int) -> None:
#         self.list.append(num)
#         self.count += 1

#     def findMedian(self) -> float:
#         if self.count == 0:
#             return 
#         self.list.sort()
        
#         if self.count % 2 != 0:
#             return self.list[(self.count//2)]
        
#         return (self.list[(self.count // 2) - 1] + self.list[(self.count // 2)] )/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()