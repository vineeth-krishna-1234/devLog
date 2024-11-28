# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        if not root:
            return False

        def dfs(root,sumValue):
            if not root:
                return False
            sumValue += root.val
            if not( root.left or  root.right) and targetSum==sumValue:
                return True
            return dfs(root.left,sumValue) or dfs(root.right,sumValue) 
        return dfs(root,0)