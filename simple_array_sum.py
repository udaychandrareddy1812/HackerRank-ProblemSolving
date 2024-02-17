def sum_fun(arr):
    count = 0
    for i in arr:
        count = count + i
        
    return count       

n = int(input())
arr = list(map(int, input().split()))

total = sum_fun(arr)
print(total)
