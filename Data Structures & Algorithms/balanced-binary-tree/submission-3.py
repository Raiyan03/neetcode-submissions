# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BalH:
    def __init__(self, b = True, h = 0):
        self.b = b
        self.h = h
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root).b
    def helper(self, root):
        if not root:
            return BalH()
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        myBalH = BalH()
        myBalH.h = max(left.h, right.h) + 1
        if left.b == False or right.b == False:
            myBalH.b = False
            return myBalH
        myBalH.b = abs(left.h - right.h) <= 1
        return myBalH
