class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combsm(idx,n,lst,ans,tmp,k):
            if n==0 and len(tmp)==k:
                ans.append(tmp[:])
                return
            if n<0:return
            for i in range(idx,len(lst)):
                combsm(i+1,n-lst[i],lst,ans,tmp+[lst[i]],k)
        lst=[i for i in range(1,10)]
        ans=[]
        tmp=[]
        combsm(0,n,lst,ans,tmp,k)
        return ans
