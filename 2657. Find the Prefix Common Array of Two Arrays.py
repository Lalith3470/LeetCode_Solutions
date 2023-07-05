class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        final=[]
        dic={}
        cnt=0
        for i in range(len(A)):
            if A[i] in dic:
                cnt+=1
            else:
                dic[A[i]]=1
            if B[i] in dic:
                cnt+=1
            else:
                dic[B[i]]=1
            final.append(cnt)
        return final
