class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # c = Counter(nums)
        # return c.most_common()[0][0]
        
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate