class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens=sorted(tokens,reverse=True)
        cnt=0
        if len(tokens)<1 or tokens[-1]>power:
            return 0
        while len(tokens)>0:
            if tokens[-1]<=power:
                a=tokens.pop()
                power-=a
                cnt+=1
            elif len(tokens)>1:
                tokens=tokens[::-1]
                a=tokens.pop()
                power+=a
                cnt-=1
                tokens=tokens[::-1]
            else:break
        return cnt
