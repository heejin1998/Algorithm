import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

sort_nums = set(nums)
sort_nums = list(sort_nums)
sort_nums.sort()

dic = {sort_nums[i] : i for i in range(len(sort_nums))}

for num in nums:
    print(dic[num], end= ' ')
print(dic)

