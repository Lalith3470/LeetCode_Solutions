class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sum = 0
        for i in range(1,int(num**(0.5)+1)):
            if num%i==0:
                sum+=i+num//i
        return sum==2*num
        
