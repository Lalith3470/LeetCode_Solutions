for _ in range(int(input())):
    a,b,c=map(int, input().split())
    if a*b<0 or b*c<0 or a*c<0:
        print("YES")
    else:
        print("NO")