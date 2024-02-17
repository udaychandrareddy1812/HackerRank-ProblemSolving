def absolute(n):
    arr_list = list()
    for i in range(n):
        x = list(map(int, input().split()))
        arr_list.append(x)
    
    #left - right sum
    count = 0
    lr_sum = 0
    for i in arr_list:
        lr_sum = lr_sum + i[count]
        count = count + 1

    #right -left sum
    count = n - 1
    rl_sum = 0
    for i in arr_list:
        rl_sum = rl_sum + i[count]
        count = count - 1
    
    return abs(lr_sum - rl_sum)

n = int(input())
diff = absolute(n)
print(diff)
