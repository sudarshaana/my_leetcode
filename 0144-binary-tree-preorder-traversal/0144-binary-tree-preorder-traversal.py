# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # recursive
#         l = []
#         self.preorder(root, l)
#         return l
    
#     def preorder(self, root, l):
#         if not root:
#             return root
#         if root:
#             l.append(root.val)
#             self.preorder(root.left, l)
#             self.preorder(root.right, l)  
        
        # iterative
        stack, output = [root], []
        
        while stack:
            item = stack.pop()
            
            if item is not None:
                output.append(item.val)

                if item.right is not None:
                    stack.append(item.right)
                if item.left is not None:
                    stack.append(item.left)
                    
        return output
            