class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return num
        
        left = 0
        right = num//2
        
        while left <=right:
            mid = left + (right-left)//2
            x =mid*mid
            
            if  x == num:
                return True
            elif x > num:
                right = mid -1
            else:
                left = mid + 1
                
        return False