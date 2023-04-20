class Solution {
public:
    void subs(int idx,vector<int>lst,vector<int>&nums,vector<vector<int>>&l,int N){
        if(idx>=N){
            l.push_back(lst);
            return ;
        }
        lst.push_back(nums[idx]);
        subs(idx+1,lst,nums,l,N);
        lst.pop_back();
        subs(idx+1,lst,nums,l,N);

    }
    vector<vector<int>> subsets(vector<int>& nums) {
        int N=nums.size();
        vector<int>lst;
        vector<vector<int>>l;
        subs(0,lst,nums,l,N);
        return l;
    }
};
