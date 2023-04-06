class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector <int> lst;
        lst.push_back(first);
        for(int i=0;i<encoded.size();i++) lst.push_back(lst[i]^encoded[i]);
        return lst;
    }
};
