class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
    
        ans = []
        
        for q in queries:
            
            way = -1
            s = 0
            for i, num in enumerate(nums):
                s+=num
                
                if num > q:
                    way = i
                    break
                
                elif s > q:
                    way = i
                    break
                    
                elif s == q:
                    way = i+1
                    break
            if way == -1:
                way = len(nums)
            ans.append(way)
                    
        return ans