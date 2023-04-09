class Solution {
public:
    int tribonacci(int n) {
        int a=1,b=0,c=0,sm=0;
        while(n>0){
            sm=a+b+c;
            a=b;
            b=c;
            c=sm;
            n--;
        }
        return c;
    }
};
