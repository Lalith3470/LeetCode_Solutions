class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None or root1.val!=root2.val:
                return False
            return solve(root1.left,root2.right) and solve(root1.right,root2.left)
        return solve(root,root)
