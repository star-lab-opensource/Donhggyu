n=10
x=[0]*42
sum=0
for i in range(n):
    a=int(input())
    y=a%42
    x[y]+=1
    if(x[y]==1):
        sum+=1
print(sum)