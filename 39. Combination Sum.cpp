class Solution {
public:
    void combs(int idx,vector<int>&arr,int target,int n,vector<int>l,vector<vector<int>>&lst){
        if(idx>n){
            if(target==0) lst.push_back(l);
            return;
        }
        l.push_back(arr[idx]);
        
        if(arr[idx]<=target){
            combs(idx,arr,target-arr[idx],n,l,lst);
        }

        l.pop_back();
        combs(idx+1,arr,target,n,l,lst);
        
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        int n=candidates.size()-1;
        vector<vector<int>>final;
        vector<int>lst;
        combs(0,candidates,target,n,lst,final);
        return final;
    }
};
