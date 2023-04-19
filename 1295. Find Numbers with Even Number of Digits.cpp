class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int evn=0;
        for(auto i:nums){
            string s=to_string(i);
            if(s.size()%2==0) evn++;
        }    
        return evn;
    }
};
