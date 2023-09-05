class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt=0
        for i in range(low,high+1):
            if len(str(i))%2==0:
                i=str(i)
                cnt+=(sum([ int(j) for j in i[len(i)//2:]]) == sum([ int(j) for j in i[:len(i)//2]]))
        return cnt
