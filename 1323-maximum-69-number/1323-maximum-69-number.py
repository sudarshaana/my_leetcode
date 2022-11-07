class Solution:
    def maximum69Number (self, num: int) -> int:
        
        new_num = []
        for i, n in enumerate(str(num)):
            if n == '6':
                new_num.append('9')
                new_num.append(str(num)[i+1:])
                break
            else:
                new_num.append(n)
        
        return int("".join(new_num))