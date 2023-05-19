class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int ln=nums.size();
        vector<int>dp(ln,1);
        for(int i=0;i<ln;i++){
            for(int j=0;j<i;j++){
                if(nums[j]<nums[i]){
                    dp[i]=max(dp[i],dp[j]+1);
                }
            }
        }
        return *max_element(dp.begin(),dp.end());
    }
};
