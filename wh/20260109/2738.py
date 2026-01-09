x,y=map(int,input().split())
a=[[0]*x for i in range(y)]
b=[[0]*x for i in range(y)]
for i in range(x):
        a[i]=list(map(int,input().split()))
for i in range(x):
        b[i]=list(map(int,input().split()))
for i in range(x):
    for j in range(y):
        a[i][j]+=b[i][j]
        print(a[i][j],end=' ')#이거 어캐내리는지 몰라서 모르는채로냄