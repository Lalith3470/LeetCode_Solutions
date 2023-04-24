class Solution {
public:
    void combs2(int idx,vector<int>&arr,int t,int sm,int n,vector<int>&tmp,vector<vector<int>>&lst){
        if(sm==t){
            lst.push_back(tmp);
            return;
        }
        for(int i=idx;i<n;i++){
            if(sm+arr[i]>t) continue;
            if(i>idx && arr[i]==arr[i-1]) continue;
            tmp.push_back(arr[i]);
            combs2(i+1,arr,t,sm+arr[i],n,tmp,lst);
            tmp.pop_back();
        }
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<int>tmp;
        vector<vector<int>>lst;
        combs2(0,candidates,target,0,candidates.size(),tmp,lst);
        return lst;
    }
};
