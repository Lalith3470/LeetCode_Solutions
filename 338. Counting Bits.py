class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            s=bin(i)
            c=0
            for j in s:
                if j == "1":
                    c+=1
            l.append(c)
        return l
