class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        num0, num1 = 0,0

        for n in nums:
            temp = max(num1, num0+n)
            num0 = num1
            num1 = temp
        return num1