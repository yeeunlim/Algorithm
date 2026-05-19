# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subRoot가 None이면 항상 참 (공집합은 모든 집합의 부분집합)
        if not subRoot: 
            return True
        # subRoot는 존재하는데 root가 None이면 부분 트리가 될 수 없음
        if not root: 
            return False
        
        # 현재 노드를 기준으로 두 트리가 같은지 확인
        if self.isSameTree(root, subRoot):
            return True
        
        # 같지 않다면, root의 왼쪽 자식이나 오른쪽 자식 중에 subRoot가 있는지 재귀적으로 탐색
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 둘 다 None이면 완전히 일치하므로 True
        if not p and not q:
            return True
        # 둘 중 하나만 None이거나, 값이 서로 다르다면 다른 트리이므로 False
        if not p or not q or p.val != q.val:
            return False
        
        # 현재 노드의 값이 같으므로, 왼쪽 자식과 오른쪽 자식도 모두 같은지 확인
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)