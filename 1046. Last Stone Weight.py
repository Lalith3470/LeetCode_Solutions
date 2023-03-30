class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort(reverse=True)
        ln=len(stones)
        while ln>=2:
            if stones[0]>stones[1]:
                stones[0]-=stones[1]
                stones.remove(stones[1])
                ln-=1
            elif stones[0]==stones[1]:
                stones.remove(stones[0])
                stones.remove(stones[0])
                ln-=2
            stones.sort(reverse=True)
        if stones:
            return stones[-1]
        else: return 0
