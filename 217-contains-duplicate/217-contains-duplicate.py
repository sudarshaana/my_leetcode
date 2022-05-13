class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data_set = set(nums)
        if len(data_set)<len(nums):
            return True
        return False