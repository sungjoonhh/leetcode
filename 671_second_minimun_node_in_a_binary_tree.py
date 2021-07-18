# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self._set = set()
        
        
        def DFS(node) -> int :

            if node :
                self._set.add(node.val)
                DFS(node.left)
                DFS(node.right)
            
        DFS(root)
        self._set.remove(min(self._set))
        
        return  min(self._set) if len(self._set) != 0 else -1