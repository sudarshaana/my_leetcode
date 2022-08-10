class Logger:

    def __init__(self):
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print_time = self.hashmap.get(message, 0)
        
        if timestamp >= print_time:
            self.hashmap[message] = 10 + timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)