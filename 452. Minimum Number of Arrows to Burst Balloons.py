class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cnt=1
        start,end=points[0][0],points[0][1]
        for i in points:
            if start<=i[0]<=end:
                start=max(start,i[0])
                end=min(end,i[1])
            else:
                cnt+=1
                start,end=i[0],i[1]
        return cnt
