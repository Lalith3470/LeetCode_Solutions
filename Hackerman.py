for _ in range(int(input())):
    a,b = map(int, input().split())
    total = a+b 
    prime = True 
    for i in range(2, total):
        if total%i==0:
            prime = False
            break 
    if prime:
        print('Alice')
    else:
        print('Bob')
