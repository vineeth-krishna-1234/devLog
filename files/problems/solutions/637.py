from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        average_array = []
        queue = deque([[root, 0]])
        current_index = 0
        temp_array = []
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            if level != current_index:
                average_array.append(sum(temp_array) / len(temp_array))
                temp_array = []
                current_index += 1
            if node:
                temp_array.append(node.val)
            queue.extend([[node.left, level + 1], [node.right, level + 1]])
        if len(temp_array):
            average_array.append(sum(temp_array) / len(temp_array))
        return average_array
