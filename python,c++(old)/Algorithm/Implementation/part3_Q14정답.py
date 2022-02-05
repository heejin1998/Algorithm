# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:03:57 2021

part3 Q14 외벽 점검

weak 리스트와 dist 리스트의 길이가 매우 작다.
주어진 데이터의 개수가 적을 때는 완전 탐색으로 접근해볼 수 있다.

원형으로 나열된 데이터를 처리하는 경우네는, 문제 풀이를 간단히 하기 위해
길이를 2배로 늘려 '원형'을 일자 형태로 만드는 작업 해주면 유리함.

"""
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
    
    #0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]
            #시작점부터 모든 취약 지점 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count+=1 # 새로운 친구 투입
                    if count>len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index]+ friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

