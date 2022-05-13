class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        c = l
        
        val = None
        
        
        while i<l:
            if nums[i] == val:
                nums.remove(val)
                nums.append(0)
                l-=1
            else:
                val = nums[i]
                i+=1
            
        return l