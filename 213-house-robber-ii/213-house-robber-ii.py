class Solution:
    def rob(self, nums: List[int]) -> int:
        
    
        if len(nums)==1:
            return nums[0]

        num0, num1 = 0,0


        for n in nums[:-1]:
            temp = max(num1, num0+n)
            num0 = num1
            num1 = temp

        m1 = num1
        num0, num1 = 0,0

        for n in nums[1:]:
            temp = max(num1, num0+n)
            num0 = num1
            num1 = temp
        return max(m1, num1)
