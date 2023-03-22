class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst=[]
        for i in range(1,rowIndex + 2):
            dp=[1]*i
            for j in range(1,i-1):
                dp[j]=lst[i-2][j]+lst[i-2][j-1]
            lst.append(dp)
        return lst[-1]
