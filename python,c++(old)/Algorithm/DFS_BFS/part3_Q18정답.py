# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:12:09 2021

@author: bobae
"""

# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0 
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        elif p[i] == ")":
            count -= 1
        
        if count == 0:
            return i 
        
# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        elif p[i] ==")":
            count -= 1
            
        if count < 0 : #올바르지 않은 문자열
            return False
    return True 

def solution(p):
    answer = ''
    if p == '': # 빈문자열인 경우
        return answer
    index = balanced_index(p)
    
    u = p[0:index+1]
    v = p[index+1:]
    
    # u가 올바른 괄호 문자열이면 v에 대해 함수를 수행한 결과 붙여 반환
    if check_proper(u) == True:
        answer = u + solution(v)
    # u가 올바른 괄호 문자열이 아니면 
    else:
        answer = '('
        answer += solution(v)
        answer +=")"
        
        u = list(u[1:-1]) # 첫번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] =='(':
                u[i] = ")"
            elif u[i] ==")":
                u[i] = "("
        answer += "".join(u)
    return answer
    