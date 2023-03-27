class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        c_sm=0
        r_sm=0
        dp=[[0]*(len(grid[0])) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:c_sm=grid[i][j]
                if i==0:
                    dp[i][j]=r_sm+grid[i][j]
                    r_sm=dp[i][j]
                elif j==0:
                    dp[i][j]=c_sm+grid[i][j]
                    c_sm=dp[i][j]
                if i!=0 and j!=0:dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]
