t = int(input())
for i in range(0,t):
    n, k = map(int, input().split())
    lis = list(map(int, input().split()))
    
    late = 0
    ontime = 0
    for j in lis:
        if j<=0:
            ontime = ontime + 1
        elif j>0:
            late = late + 1
    
    if ontime<k:
        print('YES')
    else:
        print('NO')
    
