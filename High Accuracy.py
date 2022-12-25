import math
for _ in range(int(input())):
    n=int(input())
    ans=math.ceil(n/3)*3 - n
    print(ans)
