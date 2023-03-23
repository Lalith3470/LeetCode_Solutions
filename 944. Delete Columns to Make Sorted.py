class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt=0
        for x in zip(*strs):
            a=sorted(x)
            if list(x)!=a:
                cnt+=1
        return cnt
