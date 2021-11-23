# 소수 (에라토스테네스 체)

n = int(input())
chk = [False,False]+[True]*(n-1)
result = 0
for i in range(2,n+1):
    if chk[i]:
        result +=1
        for j in range(i,n+1,i):
            chk[j]=False
print(result)