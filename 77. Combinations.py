class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst=[]
        nums=[i for i in range(1,n+1)]
        for num in combinations(nums,k):
            lst.append(num)
        return lst
