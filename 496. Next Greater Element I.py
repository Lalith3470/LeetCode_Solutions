class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    c=0
                    for k in range(j,len(nums2)):
                        if nums2[k]>nums1[i]:
                            c=nums2[k]
                            break
                    if not c:
                        l.append(-1)
                    else:
                        l.append(c)
        return l[:len(nums1)]
        
