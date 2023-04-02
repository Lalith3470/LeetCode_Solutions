class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l=[]
        for i in arr:
            if i==0:
               l+=[0,0]
            else:
                l.append(i) 
        ln=len(arr)
        arr[:]=l[:ln]
