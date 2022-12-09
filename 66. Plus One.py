class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for i in range(len(digits)):
            a+=str(digits[i])    
         
        b = str(int(a)+1)
        c = []
        for i in range(0,len(b)):
            c.append(int(b[i]))
        
        return c
