class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def shift_letter(letter, shift):
            return chr( (ord(letter)-shift) % 26 + ord('a') )
        
        
        def get_hash(string):
            shift = ord(string[0])
            return "".join( shift_letter(s, shift) for s in string)
            
        d = collections.defaultdict(list)
        
        for item in strings:
            h = get_hash(item)
            d[h].append(item)
            
        return d.values()
            