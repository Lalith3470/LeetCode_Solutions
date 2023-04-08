class CustomStack {
    vector<int>lst;
    int len=0;
public:
    CustomStack(int maxSize) {
        len=maxSize;
    }
    
    void push(int x) {
        if(lst.size()<len) lst.push_back(x);
        
    }
    
    int pop() {
        if(lst.size()==0) return -1;
        else{
        int v=lst[lst.size()-1];
        lst.pop_back();
        return v;}
    }
    
    void increment(int k, int val) {
        int ln=lst.size();
        int mn=min(ln,k);
        for(int i=0;i<mn;i++){
            lst[i]+=val;
        }
    }
};
