class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        sm=0
        val=sorted(zip(profit,difficulty),reverse=True)
        for i in worker:
            for prof,dif in val:
                if i>=dif:
                    sm+=prof
                    break
        return sm
