# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 00:01:51 2021

part3_Q02 그리디
곱하기 혹은 더하기
"""

data = input()

result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)