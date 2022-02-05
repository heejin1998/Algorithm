# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:47:38 2021

@author: bobae
"""


p = "(()())()"

def check(u): # 올바른 문자열인지 체크
    left = 0
    right = 0 
    for i in w:
        if i == "(":
            left += 1
        elif i ==")":
            right += 1
        
        if right > left: # 올바르지 않은 문자열
            return False
    return True

def dfs(w):
    if w == "": # null문자일 경우
        return w # 공백문자 자체 반환
    # 문자열 w를 균형잡힌 문자열 u, v로 분리
    left = 0 
    right = 0
    for i in w: 
        if i == "(":
            left += 1
        elif i ==")":
            right += 1
        
        if left == right:
            break
        
        u = w[0:left+right]
        v = w[left+right:]
        
        # 문자열 u가 올바른 문자열일 경우 v에 대해 1단계부터 수행
        if check(u) == True:
            dfs(v)
        # 문자열 u가 올바른 문자열이 아닌 경우
        elif check(u) == False: 
        
        
    
            