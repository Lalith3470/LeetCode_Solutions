class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frq=Counter(s)
        res=""
        for i in order:
            if i in frq:
                res+=i*frq[i]
                frq[i]=0

        for i in frq:
            res+=i*frq[i]
        return res
