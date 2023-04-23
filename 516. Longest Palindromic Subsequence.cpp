class Solution {
public:
    int palindromic(string s,string v){
        int n=s.size(),m=v.size();
        vector<vector<int>>dp(n+1,vector<int>(m+1,0));
        for(int i=1;i<n+1;i++){
            for(int j=1; j<m+1; j++){
                if(s[i-1]==v[j-1]) dp[i][j]=dp[i-1][j-1]+1;
                else dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
            }
        }
        return dp[n][m];
    }
    int longestPalindromeSubseq(string s) {
        int n=s.size(),m=s.size();
        string v=s;
        reverse(v.begin(),v.end());
        return palindromic(s,v);
    }
};
