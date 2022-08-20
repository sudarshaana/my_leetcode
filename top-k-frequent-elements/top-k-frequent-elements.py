class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # c = Counter(nums)
        # a = [key for key, _ in c.most_common(k) ]
        # return a
        
        items = {}
        for num in nums:
            items[num] = items.get(num, 0)+1
        
        q = sorted(list(items.keys()), key=lambda x: -items[x])
        return q[:k]