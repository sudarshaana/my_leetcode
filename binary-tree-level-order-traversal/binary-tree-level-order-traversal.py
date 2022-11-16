# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue, output = [(root, 1)], []
        
        while queue:
            item, level = queue.pop(0)
            #item, level = data[0], data[1]
            
            if item:
                if len(output) < level:
                    output.append([item.val])
                else:
                    output[level-1].append(item.val)
                
                if item.left:
                    queue.append((item.left, level+1))
                
                if item.right:
                    queue.append((item.right, level+1))
        return output