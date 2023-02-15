# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def ans(root):
            if not root:
                return 
            ans(root.left)
            ans(root.right)
            lst.append(root.val)
        ans(root)
        return lst
