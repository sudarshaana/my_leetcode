class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        ans = []
        
        for position, trim in queries:            
            lst = [(int(item[-trim:]), i) for i, item in enumerate(nums)]
            lst.sort()
            ans.append(lst[position-1][1])
        return ans