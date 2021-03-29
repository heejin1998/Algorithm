# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 01:15:05 2021

part3 구현
Q08 문자열 재정렬

요구하는 내용을 그대로 구현하는 문제
문자열이 입력되면, 문자를 하나씩 확인한 뒤 
숫자인 경우 따로 합계를 계산하고
알파벳인 경우 별도의 리스트에 저장

파이썬의  isalpha() 함수, isdigit() 함수, .join() 함수 새로 배움! 
"""

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))    

