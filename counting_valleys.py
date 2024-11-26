steps = int(input())
path = input()

path = path+'X'
count = 0
v_count = 0
for i in range(0,(len(path)-1)):
    if count==0:
        if path[i]=='D':
            v_count = v_count + 1
    if path[i]=='U':
        count = count+1
    elif path[i]=='D':
        count = count-1

print(v_count)
