def minmax(num):
    num.sort()
    min_sum = num[0] + num[1] + num[2] + num[3]
    max_sum = num[1] + num[2] + num[3] + num[4]

    print(min_sum, max_sum)

num = list(map(int, input().split()))

minmax(num)
