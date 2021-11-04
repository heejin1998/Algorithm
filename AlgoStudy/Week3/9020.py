chk = [False, False]+[True]*(10001)
for i in range(2, 10001):
    if chk[i]:
        for j in range(2*i,10001,i):
            chk[j] = False


t = int(input())
for l in range(t):
    result = [0, 1e9]

    n = int(input())
    for i in range(2, n-1):
        a = i
        b = n-i
        if chk[a]==True and chk[b]==True:
            if abs(result[0]-result[1]) >= abs(a-b):
                result[0] = a
                result[1] = b

    result.sort()
    print(result[0], result[1])