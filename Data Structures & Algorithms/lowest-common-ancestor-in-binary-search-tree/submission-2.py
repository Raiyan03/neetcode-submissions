# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left = min(p.val, q.val)
        right = max(p.val, q.val)

        def dfs(node):
            if not node:
                return
            
            if left <= node.val and right >= node.val:
                return node
            if left < node.val and right < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)