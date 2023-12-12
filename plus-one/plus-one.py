class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = "".join(str(i) for i in digits)
        
        number = int(number)+1
        number_str = str(number)
        
        return [int(d) for d in number_str]