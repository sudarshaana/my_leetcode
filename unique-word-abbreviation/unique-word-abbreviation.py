class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = {}
        for w in dictionary:
            if len(w)>2:
                abr = w[0] + str(len(w[1:-1])) + w[-1]
                
                saved_w = self.d.get(abr, [])
                if saved_w!=[] and saved_w == [w]:
                    continue
                self.d[abr] = self.d.get(abr, []) + [w]
                
            else:
                saved_w = self.d.get(w, [])
                if saved_w != [] and saved_w == [w]:
                    continue
                self.d[w] = self.d.get(w, []) + [w]

    def isUnique(self, word: str) -> bool:
        
        if len(word)>2:
            abr = word[0] + str(len(word[1:-1])) + word[-1]
            
        else:
            abr = word
            
        if abr not in self.d:
            return True
        
        else:
            if len(self.d[abr])>1:
                return False
            
            elif self.d[abr][0] == word:
                return True
            
            return False
            

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)