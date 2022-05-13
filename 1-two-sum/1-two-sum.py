class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        values = []
        [values.append([num, i]) for i, num in enumerate(nums)]
        values.sort()
        start, end = 0, len(nums)-1
        while start<end:
            current = values[start][0] + values[end][0]
            if target == current:
                return [values[start][1], values[end][1]]
            elif current < target:
                start+=1
            else:
                end -=1