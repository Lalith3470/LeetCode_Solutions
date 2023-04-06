class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>lst;
        int cnt=-1,i=0;
        while(i<nums.size()){
            if(nums[i]==target){
                cnt=i;
                lst.push_back(cnt);
                int val=i;
                while(val<nums.size()){
                    if(nums[val]==target) cnt=val;i++;val++;
                }
            }
            i++;
        }
        if(cnt>=0) {
            lst.push_back(cnt); 
            return lst;}
        lst.push_back(-1);
        lst.push_back(-1);
        return lst;
    }
};
