# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 06:12:47 2021

part3 구현
Q09 문자열 압축

s가 1000 이하이기 때문에 모든 경우의 수를 탐색하는 완전 탐색 수행 가능
1부터 N/2까지의 모든 수를 단위로 하여 문자열을 압축하는 방법을 모두 확인하고, 가장 짧게 압축되는 길이를 출력
"""

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count+= 1
                # 다른 문자열이 나왔다면
            else:
                compressed += str(count) + prev if count>= 2 else prev
                prev = s[j:j+step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해 처리
        compressed += str(count) + prev if count>=2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer