import sys

n = int(sys.stdin.readline())
zum = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    zum.append((y,x))

zum.sort()

for y, x in zum:
    print(x, y)
