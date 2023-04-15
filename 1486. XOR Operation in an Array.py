class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i = 0
        sum =0
        for i in range(n):
            sum ^= start + i*2
        return sum
