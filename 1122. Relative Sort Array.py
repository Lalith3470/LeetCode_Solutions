class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    l.append(arr1[j])
        s=[]
        for j in arr1:
            if j not in l:
                s.append(j)
        s.sort()
        return l+s
        
