n = int(input())

info = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    info.append((age,i,name))
info.sort()

for people in info:
    print(people[0], people[2])