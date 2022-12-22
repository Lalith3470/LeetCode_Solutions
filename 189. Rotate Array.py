class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k % len(nums)):
            nums.insert(0, nums.pop())
        nums[:] = nums
        
