class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        opening = {'(': ")", '{': "}", '[':"]"}
        for bracket in s:
            if bracket in opening.keys():
                self.stack.append(bracket)
            else:
                if self.stack:
                    saved = self.stack.pop()
                    if opening[saved] == bracket:
                        continue
                    else:
                        return False
                else:
                    return False
                
        return len(self.stack) == 0