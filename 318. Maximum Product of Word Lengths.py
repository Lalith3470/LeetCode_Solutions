class Solution:
    def maxProduct(self, words: List[str]) -> int:
        total=0
        words=list(set(words))
        cnt=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                ans=0
                for k in words[i]:
                    if k not in words[j]:ans=len(words[i])*len(words[j])
                    else:
                        ans=0
                        break
                total=max(total,ans)
        return total 
