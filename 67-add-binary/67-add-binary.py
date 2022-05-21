class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        max_len = max(len(a), len(b))
        carry = 0
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        ans = []
        for i in range(max_len-1, -1, -1):
            if a[i] == '1':
                carry+=1
            if b[i] == '1':
                carry+=1

            '''
            if both a, b and c  are 1, c is 3, we'll add 1
            if one of the 3 is 0, c will be 2 % 2 == 0 
            '''
            if carry%2 == 1: # c ==3
                ans.append("1")
            else:
                ans.append("0")
            carry //= 2

        if carry == 1:
            ans.append("1")

        ans.reverse()
        return "".join(ans)