# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 09:57:11 2021

part3 Q14 외벽 점검
1차 시도: 코드실행 에러 
"""

def clock(start, cur_dist, n, weak, direction):
    temp_count = 0
    del_weak = []
    if direction == 'right': # 시계 방향
        for i in range(start, start + cur_dist + 1):
            if i > n: 
                i -= n
            if i in weak:
                temp_count += 1
                del_weak.append(i)
    elif direction == 'left': # 반시계 방향
        for i in range(start, start + cur_dist + 1, -1):
                if i < 0: 
                    i += n
                if i in weak:
                    temp_count += 1
                    del_weak.append(i)
    return temp_count, del_weak
        
    


def solution(n, weak, dist):
    
    dist.sort() # dist가 큰 애들부터 시작
    answer = 0
    while(weak): # 취약지점 남아 있을 동안
        # dist 큰 애들이 weak 전수조사 시작
        cur_dist = dist[answer]
        for start in weak: # 어디서 시작할지
            right, del_weak_r = clock(start, cur_dist, n, weak, "right") # 시계 방향
            left, del_weak_l = clock(start, cur_dist, n, weak,  "left") # 반시계 방향
            if right > left:
                # del_weak_r에 있는거 weak에서 삭제하기
                for i in range(len(weak)):
                    if weak[i] in del_weak_r:
                        del weak[i]
            elif right < left:
                # del_weak_l에 있는거 weak에서 삭제하기
                for i in range(len(weak)):
                    if weak[i] in del_weak_l:
                        del weak[i]
        answer += 1
    return answer