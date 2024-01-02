class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt={}
        for i in nums:
            if i not in cnt:
                cnt[i]=1
            else:
                cnt[i]+=1
        lst=[]
        ln=max(cnt.values())
        for i in range(ln):
            l=[]
            for i,j in cnt.items():
                if j>=1:
                    l.append(i)
                    cnt[i]-=1
            lst.append(l)
        return lst
