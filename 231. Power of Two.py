class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        j = 0
        if n == 1:
            return True
        for i in range(len(str(n))*5):
            if pow(2,i) == n:
                j += 1
                break
        if j > 0:
            return True
        else:
            return False
