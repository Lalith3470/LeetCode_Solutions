class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=[*set(nums)]
        n.sort()
        for i in n:
            if i == target:
                return True
        else:
            return False
