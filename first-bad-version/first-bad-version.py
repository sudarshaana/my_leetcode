# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
    
        l = 1
        r = n
        while l<=r:
            mid = (l+r)//2          
            #print("{} {}  {}".format(l, r, mid))
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                r = mid
            
            elif isBadVersion(r):
                l=mid+1
            else:
                l = mid