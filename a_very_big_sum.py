def sumup(arr):
    count = 0
    for i in arr:
        count = count + i

    return count

n = int(input())
arr = list(map(int, input().split()))

x = sumup(arr)
print(x)
