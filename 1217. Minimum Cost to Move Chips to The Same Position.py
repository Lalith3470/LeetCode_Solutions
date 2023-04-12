class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt=0
        for i in position:
            if i%2==0:cnt+=1
        return min(cnt, len(position)-cnt)
