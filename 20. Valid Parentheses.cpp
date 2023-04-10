class Solution {
public:
    bool isValid(string s) {
        stack<char>stk;
        char v;
        for(int i=0;i<s.size();i++){
            if(s[i]=='[' || s[i]=='{' || s[i]=='(') stk.push(s[i]);
            else if(!stk.empty()){
                v=stk.top();
                if((s[i]==')' && v=='(') || (s[i]==']' && v=='[' ) || (s[i]=='}' && v=='{'))
                    stk.pop();
                else return false;
            }
            else if(s[i]==']' || s[i]=='}' || s[i]==')') stk.push(s[i]);
        }
        return stk.size()==0;
    }
};
