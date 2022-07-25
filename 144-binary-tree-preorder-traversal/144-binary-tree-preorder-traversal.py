# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         """ Pre-order Tree traversal with recursive function call. root -> left -> Right """
#         if root:
#             self.result.append(root.val)
#             self.preorderTraversal(root.left)
#             self.preorderTraversal(root.right)
        
#         return self.result

        """ Pre-order traversal with iterative manner"""
        stack = []
        current = root
        while current or stack:
            while current:
                self.result.append(current.val)
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            current = current.right
            
        return self.result