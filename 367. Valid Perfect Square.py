class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        n = int(math.sqrt(num))
        return n*n == num
