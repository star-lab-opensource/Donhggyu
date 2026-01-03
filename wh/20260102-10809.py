a=input()
x='abcdefghijklmnopqrstuvwxyz'
for i in len(x):
    for j in len(a):
        if(a[i]==x[i]):
            print(i)
        else:
            print(-1)