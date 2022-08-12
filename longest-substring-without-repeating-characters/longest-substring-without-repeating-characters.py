class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hashset = set()
        wordlist = []
        
        for c in s:
            if c in hashset:
                max_length = max(len(hashset), max_length)
                
                removed_char = wordlist.pop(0)
                hashset.remove(removed_char)
                while(removed_char!=c):
                    removed_char = wordlist.pop(0)
                    hashset.remove(removed_char)
                
                hashset.add(c)
                wordlist.append(c)
                    
            else:
                hashset.add(c)
                wordlist.append(c)
                
                max_length = max(len(hashset), max_length)
                
        return max_length