class Logger:

    def __init__(self):
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.hashmap:
            print_time = self.hashmap[message]
            if timestamp >= print_time:
                self.hashmap[message] = 10 + timestamp
                return True
            return False
        self.hashmap[message] = timestamp+10
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)