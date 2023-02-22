class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lst=[]
        p=sorted(p)
        for i in range(0,len(s)-len(p)+1):
            tmp=sorted(s[i:i+len(p)])
            if tmp==p:
                lst.append(i)
        return lst
