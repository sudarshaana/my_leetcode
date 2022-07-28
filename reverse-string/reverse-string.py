class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        
        def rev(s, start, end):
            if start >= end:
                return
            s[start], s[end] = s[end], s[start]
            return rev(s, start+1, end-1)
        
        rev(s, start, end)