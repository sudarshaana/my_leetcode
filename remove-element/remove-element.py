class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        i = 0
        c = l
        
        
        while i<l:
            if nums[i] == val:
                nums.remove(val)
                nums.append(0)
                l-=1
            else:
                i+=1
            
        return l