# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cnt=0
        queue=deque()
        queue.append(root)
        while queue:
            level=[]
            for i in range(len(queue)):
                tmp=queue.popleft()
                if tmp:
                    level.append(tmp.val)
                    queue.append(tmp.left)
                    queue.append(tmp.right)
            if level:
                cnt+=1
        return cnt
