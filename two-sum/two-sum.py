class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        
        for i, num in enumerate(nums):
            compliment = target-num
            if compliment in h:
                return [i, h[compliment]]
            else:
                h[num] = i
        return 