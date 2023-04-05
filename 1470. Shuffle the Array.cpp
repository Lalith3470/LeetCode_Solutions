class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector <int> lst;
        for(int i=0;i<n;i++){
            lst.push_back(nums[i]);
            lst.push_back(nums[i+n]);
        }
        return lst;
    }
};
