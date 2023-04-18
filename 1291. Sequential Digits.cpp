class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int>lst;
        for(int i=1;i<10;i++){
            string s;
            s+=to_string(i);
            for(int j=i+1;j<10;j++){
                s+=to_string(j);
                lst.push_back(stoi(s));
            }
        }
        vector<int>final;
        for(auto i:lst){
            if(i>=low && i<=high) final.push_back(i);
        }
        sort(final.begin(),final.end());
        return final;
    }
};
