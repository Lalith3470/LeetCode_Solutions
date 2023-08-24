# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic={}
        def dfs(root):
            if not root:return
            if root.left: dfs(root.left)
            v=root.val
            if v not in dic:
                dic[v]=1
            else:
                dic[v]+=1
            if root.right: dfs(root.right)

        dfs(root)
        mx=max(dic.values())
        return [i for i,j in dic.items() if j==mx]
