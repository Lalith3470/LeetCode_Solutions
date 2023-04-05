class Solution {
public:
    int twoEggDrop(int n) {
        int i=1,steps=0;
        while(n>0){
            n-=i;
            i++;
            steps++;
        }
        return steps;
    }
};
