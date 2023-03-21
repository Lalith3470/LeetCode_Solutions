class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm=[]
        cnt=0
        ln=len(s)
        for i in range(len(s)):
            if s[i]=="I":
                perm.append(cnt)
                cnt+=1
            else:
                perm.append(ln)
                ln-=1
        if s[-1]=="D":
            perm.append(cnt)
        else:
            perm.append(ln)
        return perm
