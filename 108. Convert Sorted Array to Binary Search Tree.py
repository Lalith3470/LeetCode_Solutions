# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:return None
        ln=len(nums)//2
        node=TreeNode(nums[ln])
        node.left=self.sortedArrayToBST(nums[:ln])
        node.right=self.sortedArrayToBST(nums[ln+1:])
        return node
