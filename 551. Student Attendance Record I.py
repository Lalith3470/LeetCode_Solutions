class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0
        P=0
        a=[]
        for i in s:
            if i=='L':
                L+=1
                if L==3:
                    return False
            elif i=='A':
                A+=1
                L=0
            else:
                P+=1
                L=0
        if L<3 and A<2:
            return True
        else:
            return False
