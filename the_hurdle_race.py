n, k = map(int, input().split())
height = list(map(int, input().split()))

big = 0
for i in height:
    if i>big:
        big = i

if k>=big:
    print(0)
elif k<big:
    print(big-k)
