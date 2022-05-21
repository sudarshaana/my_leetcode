class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = map(str, digits)
        number = str("".join(digits))
        result = int(number)+1
        digits = list(map(int, str(result)))
        
        return digits