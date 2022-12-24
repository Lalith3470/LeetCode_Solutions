class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in s:
                return False
            s.add(n)
        return True
