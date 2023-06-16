# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        lst=[]
        s=[]
        def dfs(root,lst,s):
            s.append(str(root.val))
            if root.left==None and root.right==None:
                lst.append("->".join(s))
                return
            if root.left:
                dfs(root.left,lst,s)
                s.pop()
            if root.right:
                dfs(root.right,lst,s)
                s.pop()

        dfs(root,lst,s)
        return lst
