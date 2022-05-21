class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hash_set = {}
        for num in arr:
            if num in hash_set:
                hash_set[num] = hash_set[num]+1
            else:
                hash_set[num] = 1
        return len(hash_set.values())==  len(set(hash_set.values()))
