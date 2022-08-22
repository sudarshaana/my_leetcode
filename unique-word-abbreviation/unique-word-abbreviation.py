class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = {}
        
        for w in dictionary:
            abr = w if len(w) <= 2 else w[0] + str(len(w[1:-1])) + w[-1]    
            if abr in self.d and self.d[abr] != w:
                self.d[abr] = "-"
            else:
                self.d[abr] = w

    def isUnique(self, w: str) -> bool:
        abr = w if len(w) <= 2 else w[0] + str(len(w[1:-1])) + w[-1]  
        
        if abr not in self.d:
            return True
        elif self.d[abr] == w:
            return True
        return False
            

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)