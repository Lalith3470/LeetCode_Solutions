class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        a=b=0
        sm=0
        if sum(gas)<sum(cost):
            return -1
        for i,j in enumerate(gas):
            sm+=j-cost[i]
            if sm<a:
                a=sm
                b=i+1   
        return b
