# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if root:
#             self.inorderTraversal(root.left)
#             #print(root.val)
#             self.result.append(root.val)
#             self.inorderTraversal(root.right)
            
#         return self.result
    
        """ Using Iterative method to traverse tree in in-order manner."""
        current = root
        stack = []
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            # list.pop() has default -1, which is the last element (recent)
            current = stack.pop()
            self.result.append(current.val)
            current = current.right
            
        return self.result