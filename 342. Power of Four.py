class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1 or n==4:
            return True
        
        for i in range(int(n/2)):
            if pow(4,i)==n:
                return True
            elif pow(4,i)>n:
                return False
