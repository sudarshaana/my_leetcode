class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = Counter(nums)
        a = [key for key, _ in c.most_common(k) ]
        return a