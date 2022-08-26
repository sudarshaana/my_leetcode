class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        w1 = -1
        w2 = -1
        res = sys.maxsize
        
        for i, word in enumerate(wordsDict):
            
            if word == word1:
                w1=i
            elif word == word2:
                w2=i
                
            if w1 != -1 and w2 != -1:
                res = min(res, abs(w2-w1))
        
        return res