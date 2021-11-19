# 자릿수의 합

n = int(input())
nums = list(input().split())

def digit_sum(x):
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    return sum
result = 0
max_sum = 0
for i in range(len(nums)):
    if max_sum < digit_sum(nums[i]):
        result = nums[i]
        max_sum = digit_sum(nums[i])
print(result)