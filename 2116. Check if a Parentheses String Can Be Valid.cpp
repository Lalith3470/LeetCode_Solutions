class Solution {
public:
    bool canBeValid(string s, string locked) {
        int csc=0,opc=0,loc=0;
        char op='(',cs=')',one='1',zro='0';
        if(s.size()%2!=0) 
            return false;
        for(int i=0; i<s.size();i++){
            if(locked[i]==one && s[i]==op) 
                opc++;
            else if(locked[i]==one && s[i]==cs) 
                csc++;
            if(locked[i]==zro) loc++;

            if(loc+opc<csc) return false;
        }
        int rsc=0,rpc=0,roc=0;
        for(int i=s.size()-1; i>=0;i--){
            cout<<i<<' ';
            if(locked[i]==one && s[i]==op) 
                rpc++;
            else if(locked[i]==one && s[i]==cs) 
                rsc++;
            if(locked[i]==zro) roc++;
            if(roc+rsc<rpc) return false;
        }
        return true;
    }
};
