a=int(input())
x=[]
n=1
nuber=1
zero=0
while(a>=n):
    nuber*=n
    n+=1
x=list(map(int,str(nuber)))
for i in range(len(x)-1,0,-1):
    if x[i]==0:
        zero+=1
    else:
        break
print(zero)