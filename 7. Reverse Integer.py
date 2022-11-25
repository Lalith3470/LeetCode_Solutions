def reverse(self, x: int) -> int:
        a = str(abs(x)).strip()
        a = int(a[::-1])
        if a > 2**31-1 or a<-2**31:
            return 0
        elif x < 0:
            return a*-1
        else:
            return a
