class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n=len(dungeon)
        m=len(dungeon[0])
        dp=[[100000]*(m+1) for _ in range(n+1)]
        dp[0][1]=1
        dp[1][0]=1
        lst=[i[::-1] for i in dungeon]
        lst=lst[::-1]
        for i in range(1,n+1):
            for j in range(1,m+1):
                tmp=min(dp[i-1][j],dp[i][j-1])-lst[i-1][j-1]
                dp[i][j]=max(tmp,1)
        #for i in dp:print(i)
        return dp[-1][-1]
