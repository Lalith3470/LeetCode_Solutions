class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        string ans;
        for(int i=0; i<s.size();i++){
            for(int j=0;j<s.size();j++){
                if(i==indices[j]) {ans+=s[j];break;}
            }
        }return ans;
    }
};
