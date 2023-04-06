class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        vector<int>lst;
        for(int i=0;i<nums.size();i++){
            lst.insert(lst.begin()+index[i],nums[i]);
        }
        return lst;
    }
};
