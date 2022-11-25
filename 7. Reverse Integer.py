def reverse(self, x: int) -> int:
        a = str(abs(x))
        a = a.strip()
        a = a[::-1]
        b = int(a)
        if b > 2**31-1 or b<-2**31:
            return 0
        elif x < 0:
            return b*-1
        else:
            return b
