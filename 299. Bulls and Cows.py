class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic=Counter(secret)-Counter(guess)
        cnt=0
        print(dic)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                cnt+=1
        cnt2=len(secret)-sum(dic.values())-cnt
        return str(cnt)+"A"+str(cnt2)+"B"
