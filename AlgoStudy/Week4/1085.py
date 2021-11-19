x, y, w, h = map(int, input().split())

# 상하좌우로 거리 구하기
res = []
res.append(x)
res.append(y)
res.append(w-x)
res.append(h-y)
print(min(res))