class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        
        target_list = []
        
        for num in nums:
            if num%2==0 and num%3==0:
                target_list.append(num)
        
        
        if not target_list:
            return 0 
        
        return int(sum(target_list)/len(target_list))