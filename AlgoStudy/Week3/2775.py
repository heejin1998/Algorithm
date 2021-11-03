t = int(input())
for l in range(t):
    # k층 n호
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            people[j] += people[j-1]
    print(people[-1])
