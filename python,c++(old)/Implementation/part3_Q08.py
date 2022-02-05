# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 00:54:08 2021

part3 구현
Q08 문자열 재정렬
"""

s = input()

str_list = []
int_list = []

for i in range(len(s)):
    if s[i].isdigit(): # 숫자일 경우
        int_list.append(int(s[i]))
    else:
        str_list.append(s[i])

str_list.sort() # 문자열을 오름차순으로 정렬        


for i in str_list:
    print(i, end='')
    
print(sum(int_list))