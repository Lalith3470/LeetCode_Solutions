class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[[1]]
        for i in range(2,numRows+1):
            dp=[1]*i
            for j in range(1,i-1):
                dp[j]=l[i-2][j]+l[i-2][j-1]
            l.append(dp)
        return l
