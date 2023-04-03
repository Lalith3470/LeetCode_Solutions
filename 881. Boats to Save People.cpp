class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(),people.end());
        int boats=0,lo=0,hi=people.size()-1;
        while(lo<=hi){
            if(people[hi]+people[lo]<=limit){
                lo++;
            }
            boats++;
            hi--;
        }
        return boats;
    }
};
