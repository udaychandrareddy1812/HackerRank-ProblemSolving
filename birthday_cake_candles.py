n = int(input())
candles = list(map(int, input().split()))

big = 0
for i in candles:
    if i >= big:
        big = i

count = 0
for i in candles:
    if i == big:
        count = count + 1
        
print(count)
