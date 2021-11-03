# 소수 구하기 - 에라토스테네스의 체 X

def check_prime(num):
    if num <2:
        return False
    for i in range(2, num):
        if num % i ==0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))

result = 0
for num in nums:
    if check_prime(num):
        result += 1
print(result)
