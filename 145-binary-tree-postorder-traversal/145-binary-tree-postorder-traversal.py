# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         stack = []
#         current = root
#         prev = None
        
#         while current or stack:
        
#             while current:
#                 stack.append(current)
#                 current = current.left
                
#             while not current and stack:
                
#                 current = stack[-1]
#                 if current.right == None or current.right == prev:
#                     stack.pop()
#                     self.result.append(current.val)
#                     prev = current
#                     current = None
#                 else:
#                     current =current.right
                    
#         return self.result
        """ Post order tree traversal. """
        if not root:
            return root
        
        stack1 = []
        stack2 = []
        stack1.append(root)
        
        while stack1:
            value = stack1.pop()
            stack2.append(value.val)
            
            if value.left:
                stack1.append(value.left)
            if value.right:
                stack1.append(value.right)
        stack2.reverse()
        return stack2