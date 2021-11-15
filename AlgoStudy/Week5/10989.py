import sys
n = int(sys.stdin.readline())
hits=[0]*10001

for i in range(n):
    hits[int(sys.stdin.readline())]+=1

for i in range(10001):
    if hits[i]:
        for j in range(hits[i]):
            print(i)
