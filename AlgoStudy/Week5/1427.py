n = input()
nums = []
for ch in n:
    nums.append(int(ch))
nums.sort(reverse=True)

for num in nums:
    print(num, end='')