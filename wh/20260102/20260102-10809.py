a=input()#abc
x='abcdefghijklmnopqrstuvwxyz'
n=-1
for i in range(len(x)):
    for j in range(len(a)):
        if(x[i]==a[j]):
            n=j
            break
        n=-1
    print(n,end=' ')