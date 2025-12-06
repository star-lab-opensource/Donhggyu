a=int(input())
people=[]
for i in range(a):
    age,name=input().split()
    people.append([int(age),name])
people.sort()
for i in range(a):
    print(people[i])