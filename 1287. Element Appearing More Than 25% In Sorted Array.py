class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans=Counter(arr)
        for i,j in sorted(ans.items(),key=lambda i: i[1],reverse=True):
            if j>=len(ans)*0.25:
                return i
            
