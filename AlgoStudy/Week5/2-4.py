n = int(input())
scores = list(map(int, input().split()))
# round는 round_half_even 방식을 택한다. -> round 쓰는거 위험할 수 있음
#avg = round(sum(scores)/len(scores))
avg = sum(scores)/n
avg += 0.5
avg = int(avg)

# 정렬 순서 - 차이(abs), 높은점수, 학생번호 빠른순
min = 247000000
for idx, score in enumerate(scores):
    diff = abs(avg-score)
    if min > diff:
        min = diff
        res_score = score
        res = idx +1
    elif min==diff:
        if res_score < score:
            res_score = score
            res = idx+1
print(avg, res)




