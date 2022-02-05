# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 01:22:10 2021

2021 KAKAO BLIND
신규 아이디 추천 (Level 1)
"""

def solution(new_id):
    
    answer = ''
    # 1단계
    answer = new_id.lower()
    
    # 2단계
    for word in answer:
        if word.isalnum() or word in '-_.':
            continue
        else:
            answer = answer.replace(word, "")
  
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
   
    # 4단계
    answer = answer.strip('.')
   
    
    # 5단계
    if answer =="":
        answer = "a"
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14]=='.':
            answer = answer[:14]
    
    # 7단계
    if len(answer)<=2:
        while len(answer) < 3:
            answer += answer[-1]
        
    return answer

new_id = "abcdefghijklmn.p"
result = solution(new_id)
print(result)