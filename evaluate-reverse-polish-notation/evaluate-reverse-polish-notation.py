

class Solution:
    
    def  result(self, n1, n2, op):
        if op == '+':
            return n1+n2
        elif op == '-':
            return n1-n2
        elif op == '*':
            return n1*n2
        else:
            return int(n1 / n2)
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')
        r = None
        
        for item in tokens:
            if item not in operators:
                stack.append(item)
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                
                r = self.result(int(val1), int(val2), item)
                #print(r)
                #print(val1, item, val2, r)
                stack.append(r)
        
        return int(stack.pop())