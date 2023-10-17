class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n, ans = len(nums), [-1,-1]
        for i in range(n):
            for j in range(n):
                if abs(i-j) >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    ans = [i,j]

        return ans
