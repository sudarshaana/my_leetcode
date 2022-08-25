class SparseVector:
    def __init__(self, nums: List[int]):
        self.num1 = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        
        total = 0
        for n1, n2 in zip(self.num1, vec.num1):
            total += (n1*n2)
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)