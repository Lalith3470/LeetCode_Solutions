class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        val=prices[0]
        cnt=0
        for i in range(1,len(prices)):
            cost=prices[i]-val
            if cnt<cost:
                cnt=cost
            val=min(val,prices[i])
        return cnt
        
