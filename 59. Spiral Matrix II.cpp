class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>>dp(n,vector<int>(n,0));
        int cnt=1;
        int top=0,bottom=n-1,left=0,right=n-1;
        while(top<=bottom && left<=right){
            for(int i=left;i<=right;i++){
                dp[top][i]=cnt;
                cnt++;
            }
            top++;
            for(int i=top;i<=bottom;i++){
                dp[i][right]=cnt;
                cnt++;
            }
            right--;
            if(top<=bottom){
                for(int i=right;i>=left;i--){
                    dp[bottom][i]=cnt;
                    cnt++;
                }
            }
            bottom--;
            if(left<=right){
                for(int i=bottom;i>=top;i--){
                    dp[i][left]=cnt;
                    cnt++;
                }
            }
            left++;
        }
        return dp;

    }
};
