class Solution:
    def canPermutePalindrome(self, string: str) -> bool:
        
        counter = Counter(self.clean(string))
        return sum(c%2 for c in counter.values()) <= 1
    
    def clean(self, s):
        return [c for c in s.lower() if c in string.ascii_lowercase]    