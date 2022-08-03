class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmap = {}
        
        for i, num in enumerate(nums):
            if not num in hashmap:
                hashmap[num] = i
            else:
                saved_index = hashmap[num]
                if abs(i-saved_index) <=k:
                    return True
                else:
                    hashmap[num] = i
        return False