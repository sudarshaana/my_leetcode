class Solution:
    def canPermutePalindrome(self, string: str) -> bool:
        string = string.lower()
        hashset = set()

        for s in string:
            if s == " ":
                continue
            elif s not in hashset:
                hashset.add(s)
            else:
                hashset.remove(s)

        if len(hashset) == 0:
            return True
        elif len(hashset) % 2 !=0 and len(hashset) == 1:
            return True

        else:
            return False