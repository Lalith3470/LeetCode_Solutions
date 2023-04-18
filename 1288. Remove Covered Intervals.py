class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(0))
        ln=len(intervals)
        cp=intervals.copy()
        for i in cp:
            for j in cp:
                if j[0]<=i[0] and i[1]<=j[1] and i!=j:
                    ln-=1
                    intervals.remove(i)
                    break
        return ln
