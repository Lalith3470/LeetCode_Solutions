class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1 or n == 3:
            return True
        for i in range(int(n/3)):
            if 3**i==n:
                return True
            elif 3**i>n:
                return False
