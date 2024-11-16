q = int(input())

for i in range(q):
    x,y,z = map(int,input().split())
    d1 = abs(z-x)
    d2 = abs(z-y)
    if d1>d2:
        print('Cat B')
    elif d2>d1:
        print('Cat A')
    elif d1 == d2:
        print('Mouse C')
