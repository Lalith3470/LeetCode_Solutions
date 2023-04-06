class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector <int> lst;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums[i];j++) lst.push_back(nums[i+1]);
            i++;
        }
        return lst;
    }
};
