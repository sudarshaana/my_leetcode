# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def successor(self, root):
        """ Successor is the smallest child of the right node. """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """ Predecessor is the largest child of the left node. """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        # let's find the node, is it in left or right or just current node
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        else: # found it!!!!
            
            # is it a leaf node?
            if not root.left and not root.right:
                root = None # deleted!!!
            
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                
        return root
