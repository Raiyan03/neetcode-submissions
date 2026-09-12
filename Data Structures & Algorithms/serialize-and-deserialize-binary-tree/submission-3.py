# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = []
        def dfs(node):
            if not node:
                ser.append('N')
                return
            ser.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(ser)       
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.idx = -1
        self.splitData = data.split(',')
        
        def dfs():
            self.idx += 1
            if self.idx >= len(self.splitData) or self.splitData[self.idx] == 'N':
                return
            
            node = TreeNode(self.splitData[self.idx])
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()









