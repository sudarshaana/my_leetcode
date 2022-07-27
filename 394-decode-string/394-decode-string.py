class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        digit_last = False
        for c in s:
            if c != ']':
                if c.isdigit() and digit_last:
                    val = stack.pop()
                    stack.append(val+c)
                else:
                    stack.append(c)
                
                if c.isdigit():
                    digit_last = True
                else:
                    digit_last = False
                    
            else:
                string = ""
                digit = None
                while string=="" or digit == None:
                    val = stack.pop()
                    if val == '[':
                        pass
                    elif val.isdigit():
                        digit = int(val)
                    else:
                        string  =  val + string
                stack.append(string*digit)
                
        return ''.join(stack)