# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:51:03 2021

실전문제 3. 성적이 낮은 순서로 학생 출력하기
p. 180

학생의 정보가 최대 100,000개까지 입력될 수 있으므로 계수 정렬을 이용.
혹은 파이썬의 기본 정렬 라이브러리를 사용하는 것이 효과적.
"""

n = int(input())

array = []

for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))
    
# 키를 이용하여 점수를 정렬으로 기준
array = sorted(array, key = lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = ' ')