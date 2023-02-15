# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def ans(root):
            if not root:
                return 
            lst.append(root.val)
            ans(root.left)
            ans(root.right)
        ans(root)
        return lst
