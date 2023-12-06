class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        even_count = 0
        for num in nums:   
            
            digit_count = int(math.floor(math.log10(num))) + 1
            if digit_count%2 == 0:
                even_count+=1
                
        return even_count