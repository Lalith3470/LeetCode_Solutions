class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ln=heights.copy()
        ln.sort()
        count=0
        for i in range(len(heights)):
            if heights[i]!=ln[i]:
                count+=1
        return count
