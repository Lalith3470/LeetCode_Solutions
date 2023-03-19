class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sm=0
        lst=[max(i) for i in zip(*grid)]
        lst1=[max(i) for i in grid]
        for i in range(len(grid)):
            for j in range(len(grid)):
                sm+=min(lst[j],lst1[i])-grid[i][j]
        return sm
