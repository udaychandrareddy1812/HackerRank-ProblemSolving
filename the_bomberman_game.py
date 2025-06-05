import copy

r,c,n = map(int,input().split())
ism = list()
for i in range(r):
    x = input()
    ism.append(x)

ism1 = ism
ism2 = list()
for i in range(r):
    ism2.append(c*'O')    

co_lis = list()
for i in range(r):
    for j in range(c):
        if ism[i][j]=='O':
            co_lis.append((i,j))

ncell_lis = list()
for i in co_lis:
    ncell_lis.append((i[0]+1,i[1]))
    ncell_lis.append((i[0]-1,i[1]))
    ncell_lis.append((i[0],i[1]+1))
    ncell_lis.append((i[0],i[1]-1))

for i in ncell_lis:
    if i[0]<0 or i[1]<0:
        ncell_lis.remove(i)

ism3 = copy.deepcopy(ism2)

for i in range(len(ism)):
    x = list(ism3[i])
    ism3[i] = x

for i in co_lis:
    try:
        if ism3[i[0]][i[1]] == 'O':
            ism3[i[0]][i[1]] = '.'      
    except IndexError:
        pass

for i in ncell_lis:
    try:
        if ism3[i[0]][i[1]] == 'O':
            ism3[i[0]][i[1]] = '.'
    except IndexError:
        pass

co_lis=list()
for i in range(r):
    for j in range(c):
        if ism3[i][j]=='O':
            co_lis.append((i,j))

ncell_lis = list()
for i in co_lis:
    ncell_lis.append((i[0]+1,i[1]))
    ncell_lis.append((i[0]-1,i[1]))
    ncell_lis.append((i[0],i[1]+1))
    ncell_lis.append((i[0],i[1]-1))
    
for i in ncell_lis:
    if i[0]<0 or i[1]<0:
        ncell_lis.remove(i)

ism5 = copy.deepcopy(ism2)

for i in range(len(ism)):
    x = list(ism5[i])
    ism5[i] = x
    
for i in co_lis:
    try:
        if ism5[i[0]][i[1]] == 'O':
            ism5[i[0]][i[1]] = '.'      
    except IndexError:
        pass

for i in ncell_lis:
    try:
        if ism5[i[0]][i[1]] == 'O':
            ism5[i[0]][i[1]] = '.'
    except IndexError:
        pass
        
for i in range(len(ism3)):
    x = [''.join(ism3[i])]
    ism3[i] = x
ism3 = [item[0] for item in ism3]

for i in range(len(ism5)):
    x = [''.join(ism5[i])]
    ism5[i] = x
ism5 = [item[0] for item in ism5]

if n==1:
    for i in ism1:
        print(i)
elif n%2==0:
    for i in ism2:
        print(i)
elif n%4==3:
    for i in ism3:
        print(i)
elif n%4==1:
    for i in ism5:
        print(i)
