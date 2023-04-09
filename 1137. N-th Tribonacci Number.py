class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c=1,0,0
        for i in range(n):
            tmp=a+b+c
            a=b
            b=c
            c=tmp
        return c
