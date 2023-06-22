# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic=defaultdict(list)
        def dfs(root,cnt,lvl):
            if not root:return
            dic[cnt].append((root.val,lvl))
            if(root.left): dfs(root.left,cnt-1,lvl+1)
            if(root.right): dfs(root.right,cnt+1,lvl+1)
        dfs(root,0,0)
        final=[]
        for i,j in sorted(dic.items()):
            final.append([v[0] for v in sorted(j,key=operator.itemgetter(1,0))])
        return final
