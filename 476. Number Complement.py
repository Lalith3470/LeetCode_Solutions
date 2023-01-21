class Solution:
    def findComplement(self, num: int) -> int:
        s=str(bin(num).replace("0b", ""))
        a=''
        for i in s:
            if i=='1':
                a+='0'
            else:
                a+='1'
        return int(a,2)
