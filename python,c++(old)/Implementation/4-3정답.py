# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:26:41 2021
p. 117
실전 2. 왕실의 나이트
"""
#현재 나이트의 위치 입력 받기
input_data = input()
column = int(ord(input_data[0]))- int(ord('a')) + 1
row = int(input_data[1])

#s 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향에 대해 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result +=1
print(result)
