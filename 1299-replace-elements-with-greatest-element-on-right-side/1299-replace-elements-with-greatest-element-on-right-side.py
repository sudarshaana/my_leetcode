class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        last = arr[-1]
        maxlast = -1
        ar_l = len(arr)
        
        for i in range(ar_l-1,-1,-1):
             
            last = arr[i]
            arr[i] = maxlast
            
            maxlast = max(maxlast, last)
        
        return arr