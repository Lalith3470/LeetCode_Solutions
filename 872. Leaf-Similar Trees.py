# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1=[]
        l2=[]
        def dfs(root):
            if root.left==None and root.right==None:
                l1.append(root.val)
            if root.left:dfs(root.left)
            if root.right:dfs(root.right)
        def dfs1(root):
            if root.left==None and root.right==None:
                l2.append(root.val)
            if root.left:dfs1(root.left)
            if root.right:dfs1(root.right)
        dfs(root1)
        dfs1(root2)

        return l1==l2
