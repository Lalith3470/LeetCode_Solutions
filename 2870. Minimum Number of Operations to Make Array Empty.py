class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic=Counter(nums)
        total=0
        for i,j in dic.items():
            if j==1:return -1
            tmp=j//3
            total+=tmp if j%3==0 else tmp+1
        return total
