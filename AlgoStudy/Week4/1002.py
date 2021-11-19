import math
T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

    if distance ==0 and r1==r2: # 동심원
        print(-1)
    elif abs(r1-r2)== distance or r1+r2==distance: # 내접, 외접
        print(1)
    elif abs(r1-r2)<distance<(r1+r2): # 서로다른 두 점
        print(2)
    else:               # 그 외
        print(0)


