class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nu=nums1[:m]
        nu2=nums2[:n]
        final = nu+nu2
        final.sort()
        nums1[:]=final
