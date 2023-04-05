class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector <int> lst;
        for(int i=0; i<nums.size();i++){
            int a=nums[i];
            lst.push_back(nums[a]);
        }
        return lst;
    }
};
