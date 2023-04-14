class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dic={}
        mx=0
        ln=len(arr)
        for i in range(ln):
            dic[arr[i]]=i
        dp=[[0]*(ln) for j in range(ln)]
        for i in range(0,ln):
            for j in range(i+1,ln):
                a=i
                b=j
                while b<ln:
                    sm=arr[a]+arr[b]
                    if sm in dic:
                        a=b
                        b=dic[sm]
                        dp[a][b]+=1
                        mx=max(dp[a][b],mx)
                    else:break
        return mx+2 if mx!=0 else 0
