class Solution:
    def fib(self, n: int) -> int:
        l=[0,1]
        n1=0
        n2=1
        for i in range(2,n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            l.append(n3)
        if n>0:
            return l[-1]+l[-2]
        else:
            return 0
