import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

# 산술평균
print(round(sum(nums)/len(nums)))
# 중앙값
nums.sort()
print(nums[int(len(nums)/2)])
# 최빈값 - Counter를 사용하여 요소의 개수를 세어줌
# most_common()은 빈도수가 높은 순으로 리스트 안의 튜플 형태로 반환
cnt = Counter(nums).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

# 범위
print(max(nums)-min(nums))