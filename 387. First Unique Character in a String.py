class Solution:
    def firstUniqChar(self, s: str) -> int:
        l={}
        for i in s:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for i in s:
            if l[i]==1:
                return s.index(i)
        return -1
		
