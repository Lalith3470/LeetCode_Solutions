class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums=nums[::-1]
        return nums[k-1]
