class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=2:return 1
        if n==3: return 2
        tmp=1
        while n>4:
            tmp*=3
            n-=3
        return tmp*n
