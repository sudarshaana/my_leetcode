import math
class Solution:
    def isThree(self, n: int) -> bool:
        
        
        divisor_count = 1
        
        for i in range(int(math.sqrt(n))):
            
            if n % (i+1) == 0:
                divisor_count+=1
                if i != 0 and (i+1 != int(n/(i+1))):
                    divisor_count+=1
                
            if divisor_count > 3:
                return False
            
        if divisor_count == 3:
            return True