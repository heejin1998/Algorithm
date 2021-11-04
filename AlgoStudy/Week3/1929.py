m, n = map(int, input().split())
chk = [False, False] + [True] * (n-1)
primes = []
for i in range(2, n+1):
    if chk[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            chk[j] = False
for prime in primes:
    if prime >=m and prime <= n:
        print(prime)

