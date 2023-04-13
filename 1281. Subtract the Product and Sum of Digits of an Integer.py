class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        product = 1
        sum = 0
        for i in range(len(s)):
            product *= int(s[i])
            sum += int(s[i])
        return (product-sum)
