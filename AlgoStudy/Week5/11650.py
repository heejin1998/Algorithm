n = int(input())

zum = []
for i in range(n):
    x, y = map(int, input().split())
    zum.append((x,y))

zum.sort()
for x, y in zum:
    print(x, y)