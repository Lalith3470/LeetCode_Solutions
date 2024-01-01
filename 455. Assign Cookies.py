class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res=0
        i=0
        for idx in g:
            while i<len(s) and s[i]<idx:
                i+=1
            if i==len(s): 
                return res
            i+=1
            res+=1
        return res
