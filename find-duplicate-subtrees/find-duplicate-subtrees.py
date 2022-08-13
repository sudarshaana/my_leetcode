# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        ans = []
        hashmap = {}
        
        def find(root, path):
            if not root:
                return '#'
            
            path += ','.join([str(root.val), find(root.left, path), find(root.right, path)])
            
            if path in hashmap:
                hashmap[path]+=1
                if hashmap[path] == 2:
                    ans.append(root)
            else:
                hashmap[path] = 1
                
            return path
            
            
        find(root, "")
        return ans
            