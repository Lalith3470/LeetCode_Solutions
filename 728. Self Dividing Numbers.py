class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            a=str(i)
            c=0
            for j in a:
                if int(j)!=0 and int(a)%int(j)==0:
                    c+=1
            if c==len(a):
                l.append(i)
        return l
