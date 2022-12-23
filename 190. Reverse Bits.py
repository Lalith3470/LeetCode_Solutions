class Solution:
    def reverseBits(self, n: int) -> int:
        n="{:032b}".format(n)
        a=str(n)
        a=a[::-1]
        return int(a,2)
