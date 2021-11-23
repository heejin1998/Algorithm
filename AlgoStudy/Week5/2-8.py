# 뒤집은 소수
'''
강의 코드
def reverse(x):
    res=0
    while x > 0:
        t = x % 10
        res = res*10+t
        x= x//10
    return res
'''

def reverse(x):
    answer = ""
    for i in range(len(x)-1,-1,-1):
        answer += x[i]
    return answer


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1): # 소수 체크는 절반까지만 해도 됨
        if x % i==0:
            return False
    return True


n = int(input())

nums = list(input().split())
for num in nums:
    reverse_num = int(reverse(num))
    if isPrime(reverse_num):
        print(reverse_num, end=' ')




