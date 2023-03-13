class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq={}
        s1=s1.split()
        s2=s2.split()
        s=s1+s2
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        lst=[]
        for i,j in freq.items():
            if j==1:
                lst.append(i)
        return lst
