# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')
        def get_max_gain(node):
            if node == None:
                return 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            curr_sum = left_gain + right_gain + node.val
            self.max_path_sum = max(self.max_path_sum, curr_sum)

            return node.val + max(left_gain, right_gain)
        get_max_gain(root)
        return self.max_path_sum