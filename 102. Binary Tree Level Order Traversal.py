# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        queue.append(root)
        lst=[]
        while queue:
            levels=[]
            for i in range(len(queue)):
                node=queue.popleft()
                if node:
                    levels.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if levels:
                lst.append(levels)
        return lst
