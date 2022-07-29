# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #MAX = 1
        def calculate(root, dept):
            if not root:
                return dept
            
            return max(calculate(root.left, dept+1), calculate(root.right, dept+1))
        
        return calculate(root, 0)
        
        
        