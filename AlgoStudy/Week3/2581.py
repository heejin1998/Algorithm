# 소수
m = int(input())
n = int(input())
primes = []

for i in range(m,n+1):
    if i!=1:
        check = True
        for j in range(2,i):
            if i % j == 0:
                check=False
                break
        if check:
            primes.append(i)

if len(primes)==0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
