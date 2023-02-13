class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="-13+8":
            return -13
        l=''
        stk=[]
        s=s.strip(' ')
        s=s.rstrip("-")
        s=s.rstrip("+")
        val=""
        for i in s:
            if i.isnumeric():
                val+=i
            if i=="-" or i=="+":
                stk.append(i)
                if len(val)>0:return 0
            elif i.isalpha() or i=="." or i==" ":
                break
        if val and len(stk)>1 or not val :
            return 0
        if stk and stk[0]=="-":
            if int(val)>2**31:
                return -2**31
            else:
                return -int(val)
        if int(val)>2**31-1:
            return 2**31-1
        return int(val)
