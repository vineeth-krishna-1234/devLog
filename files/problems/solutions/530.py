# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_value = float("inf")
        self.previous_value = -float("inf")

        def in_order_traversal(root):
            if root:
                in_order_traversal(root.left)
                self.min_value = min(
                    self.min_value, abs(self.previous_value - root.val)
                )
                self.previous_value = root.val
                in_order_traversal(root.right)

        in_order_traversal(root)
        return self.min_value
