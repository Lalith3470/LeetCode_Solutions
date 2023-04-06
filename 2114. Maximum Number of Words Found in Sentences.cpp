class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int mx=0;
        for(int i=0;i<sentences.size();i++){
            int cnt=count(sentences[i].begin(),sentences[i].end(),' ');
            mx=max(cnt+1,mx);
        }
        return mx;
    }
};
