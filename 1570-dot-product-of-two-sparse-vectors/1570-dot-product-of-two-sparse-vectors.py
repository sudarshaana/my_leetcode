class SparseVector:
    def __init__(self, nums: List[int]):
        #self.num1 = nums
        self.num1 = {i:val for i, val in enumerate(nums) if val != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        
        total = 0
        # for n1, n2 in zip(self.num1, vec.num1):
        #     total += (n1*n2)
        for k, v in self.num1.items():
            if k in vec.num1:
                total+=v*vec.num1[k]
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)