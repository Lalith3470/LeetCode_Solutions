class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        stack<int>stk;
        int ln=heights.size(),mx=0;
        for(int i=0; i<ln; i++){
            while(!stk.empty() && heights[stk.top()]>=heights[i]){
                int ht=heights[stk.top()];
                stk.pop();
                int wt=0;
                if(!stk.empty()) wt=i-stk.top()-1;
                else wt=i;
                mx=max(mx,ht*wt);
            }
            stk.push(i);
        }
        return mx;
        
    }
};
