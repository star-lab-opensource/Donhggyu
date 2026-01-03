t = int(input())
for i in range(t):
    floor=int(input())
    room=int(input())
    people=[]
    for i in range(room+1):
        people.append(i)
    for i in range(floor):
        for j in range(1,room+1):
            people[j]=people[j]+people[j-1]
    print(people[room])