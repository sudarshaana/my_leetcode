class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        
        found = False
        
        for char in letters:
            if char == target:
                found = True
            elif ord(char)>ord(target):
                return char
            if found and char != target:
                return char
        
        return letters[0]