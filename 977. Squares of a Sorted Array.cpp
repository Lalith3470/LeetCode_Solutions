class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int>lst;
        for(auto i:nums){
            lst.push_back(pow(i,2));
        }
        sort(lst.begin(),lst.end());
        return lst;
    }
};
