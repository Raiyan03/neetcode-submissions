# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Diam:
    def __init__(self, h = 0, d = 0):
        self.h = h
        self.d = d
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameter(root).d

    def diameter(self, root: Optional[TreeNode]) -> int:
        if not root:
            return Diam()
        Diamleft = self.diameter(root.left)
        Diamright = self.diameter(root.right)
        Diamroot = Diamleft.h + Diamright.h

        myDiam = Diam()
        myDiam.h = max(Diamleft.h, Diamright.h) + 1
        myDiam.d = max(Diamleft.d, Diamright.d, Diamroot)

        return myDiam