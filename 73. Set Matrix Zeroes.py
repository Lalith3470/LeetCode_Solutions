class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dp=[[1]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for c in range(len(matrix)):
                        dp[c][j]=0
                    for c in range(len(matrix[0])):
                        dp[i][c]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j]!=0:
                    dp[i][j]=matrix[i][j]       
        matrix[:]=dp
