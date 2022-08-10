class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmap = set()
        for i, num in enumerate(nums):
            if num in hashmap:
                return True
            else:
                hashmap.add(num)
                if len(hashmap) > k:
                    hashmap.remove(nums[i-k])
                
        return False
        
        # for i, num in enumerate(nums):
        #     if not num in hashmap:
        #         hashmap[num] = i
        #     else:
        #         saved_index = hashmap[num]
        #         if abs(i-saved_index) <=k:
        #             return True
        #         else:
        #             hashmap[num] = i
        # return False