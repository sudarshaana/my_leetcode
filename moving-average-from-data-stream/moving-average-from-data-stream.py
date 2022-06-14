class MovingAverage:

    def __init__(self, size: int):
        self.number = size
        self.queue = []

    def next(self, val: int) -> float:
        if len(self.queue) == self.number:
            self.queue.pop(0)
        self.queue.append(val)
        return sum(self.queue)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)