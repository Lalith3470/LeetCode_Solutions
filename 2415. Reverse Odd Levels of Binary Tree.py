# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        cnt=0
        queue=deque()
        queue.append(root)
        lst=[]
        while queue:
            ln=len(queue)
            if cnt%2!=0:
                st=0
                end=len(queue)-1
                while st<end:
                    queue[end].val,queue[st].val=queue[st].val,queue[end].val
                    st+=1
                    end-=1
            for _ in range(ln):
                node=queue.popleft()
                if node:
                    if node.left:queue.append(node.left)
                    if node.right:queue.append(node.right)
            cnt+=1
        return root
