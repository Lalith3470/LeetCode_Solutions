class Solution {
public:
    int numTilings(int n) {
        vector<long long>dp(n+3,0);
        if(n<2) return n;
        dp[0]=1;dp[1]=2;dp[2]=5;
        const long long mod=1e9+7;
        for(int i=3;i<n;i++){
            dp[i]=(dp[i-1]*2+dp[i-3])%mod;
        }
        return dp[n-1];
    }
};
