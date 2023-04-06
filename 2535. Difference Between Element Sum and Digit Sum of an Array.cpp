class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int sm=0,diff=0;
        for(auto i: nums){
            sm+=i;
            while(i>0){
                diff+=i%10;
                i/=10;
            }
        }return abs(sm-diff);
    }
};
