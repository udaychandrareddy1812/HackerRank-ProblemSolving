s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apple = list(map(int, input().split()))
orange = list(map(int, input().split()))

apple_count = 0
orange_count = 0

for i in apple:
    if ((a+i)>=s and (a+i)<=t):
        apple_count = apple_count + 1

for i in orange:
    if ((b+i)>=s and (b+i)<=t):
        orange_count = orange_count + 1

print(apple_count)
print(orange_count)
