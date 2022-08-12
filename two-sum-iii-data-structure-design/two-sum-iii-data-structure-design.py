class TwoSum:

    def __init__(self):
        self.s = {}

    def add(self, number: int) -> None:
        self.s[number] = self.s.get(number, 0)+1

    def find(self, value: int) -> bool:
        
        for n in self.s.keys():
            req_digit = value - n
            
            if n!= req_digit:
                if req_digit in self.s:
                    return True
            else:
                if self.s[req_digit]>1:
                    
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)