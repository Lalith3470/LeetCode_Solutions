class Solution:
    def fib(self, n: int) -> int:
        prev,prev2=1,0
        if n==0: return prev2
        for i in range(2,n+1):
            curr=prev+prev2
            prev,prev2=curr,prev
        return prev
        
