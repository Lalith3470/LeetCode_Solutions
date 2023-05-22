class Solution:
    def maximum69Number (self, num: int) -> int:
        
        l=[num]
        for i in range(len(str(num))):
            s=str(num)
            if s[i]=="9":
                s=s[:i]+"6"+s[i+1:]
            else:
                s=s[:i]+"9"+s[i+1:]
            l.append(int(s))
        return max(l)
        
