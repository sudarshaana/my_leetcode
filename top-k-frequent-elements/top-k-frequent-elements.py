class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        # ----- using bucket sort ----
        items = {}
        for num in nums:
            items[num] = items.get(num, 0)+1
        
        buckets = [[] for _ in range(len(nums))]
        
        for key, v in items.items():
            buckets[v-1].append(key)
        
        ans = []
        for bucket in buckets[::-1]:
            if bucket:
                ans.extend(bucket)
        
        return ans[:k]
        
#         heap = data
#         heapq.heapify(heap)
#         ans = []
#         for item in range(k):
#             x = heapq.heappop(heap)
#             ans.append(x[1])
        
#         return ans
        
        
        
        
        # c = Counter(nums)
        # a = [key for key, _ in c.most_common(k) ]
        # return a
        
#         items = {}
#         for num in nums:
#             items[num] = items.get(num, 0)+1
        
#         q = sorted(list(items.keys()), key=lambda x: -items[x])
#         return q[:k]

# using heap
#         items = {}
#         for num in nums:
#             items[num] = items.get(num, 0)+1
        
#         data = [(-v, k) for k, v in items.items()]
        
#         heap = data
#         heapq.heapify(heap)
#         ans = []
#         for item in range(k):
#             x = heapq.heappop(heap)
#             ans.append(x[1])
        
#         return ans