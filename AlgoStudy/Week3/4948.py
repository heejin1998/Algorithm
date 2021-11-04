while True:
    n = int(input())
    if n == 0:
        break
    primes=[]
    chk = [False, False]+[True]*(2*n+1)
    for i in range(2,2*n+1):
        if chk[i]:
            primes.append(i)
            for j in range(2*i,2*n+1,i):
                chk[j]=False
    result = []
    for prime in primes:
        if prime > n and prime <=2*n:
            result.append(prime)
    print(len(result))