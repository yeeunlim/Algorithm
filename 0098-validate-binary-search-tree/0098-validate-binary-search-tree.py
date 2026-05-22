# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            # 왼쪽 자식은 현재 노드의 값보다 작아야 하므로 high를 node.val로 갱신
            # 오른쪽 자식은 현재 노드의 값보다 커야 하므로 low를 node.val로 갱신
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root, float('-inf'), float('inf'))