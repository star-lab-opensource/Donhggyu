n=int(input())
people=[]
for i in range(n):
    age,name=input().split()
    people.append([int(age),name])
people.sort()
for i in range(n):
    print(people[i])