# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        lst=[]
        def dfs(root,tsm,sm,lst,l):
            sm+=root.val
            l.append(root.val)
            if root.left==None and root.right==None and sm==tsm:
                lst.append(l[:])
                return True
            if root.left==None and root.right==None:
                return False
            if root.left:
                dfs(root.left,tsm,sm,lst,l)
                l.pop()
            if root.right:
                dfs(root.right,tsm,sm,lst,l)
                l.pop()
        if not root:return []
        lst=[]
        sm=0
        dfs(root,targetSum,sm,lst,[])
        return lst
