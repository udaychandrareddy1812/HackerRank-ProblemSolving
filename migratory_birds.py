n = int(input())
arr = list(map(int, input().split()))

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0

for i in arr:
    if i == 1:
        count_1 = count_1 + 1
    elif i == 2:
        count_2 = count_2 + 1
    elif i == 3:
        count_3 = count_3 + 1
    elif i == 4:
        count_4 = count_4 + 1
    elif i == 5:
        count_5 = count_5 + 1
        
lis = [count_1, count_2, count_3, count_4, count_5]
x = lis.index(max(lis))

print(x + 1)
