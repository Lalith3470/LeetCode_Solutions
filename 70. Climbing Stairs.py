class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        for i in range(n-1):
            t=a
            a+=b
            b=t
        return a
