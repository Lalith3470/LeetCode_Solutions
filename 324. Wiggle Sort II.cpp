class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int>lst;
        int ln=nums.size()-1,mid,tmp;
        mid=ln/2;
        tmp=mid;
        while(mid>=0)
        {
            lst.push_back(nums[mid--]);
            if(ln>tmp)
               lst.push_back(nums[ln--]);
        }
        nums=lst;
    }
};
