# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:53:37 2021

솔!
"""
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]



def get_distance(places, r, c):
    for i in range(5):
        for j in range(5):
            if places[i][j] == 'P':
                dist = abs(r-i) + abs(c - j)
                if dist > 2:
                    return True
                if dist == 1: # 맨해튼 거리가 1인 경우
                    return False
                if dist == 2: # 맨해튼 거리가 2인 경우
                    if c == j: # 같은 행인 경우
                        if places[(r+i)//2][j] == 'X': # 파티션 있을 경우
                            break
                        else:
                            return False
                    elif r == i: # 같은 열인 경우
                        if places[r][(c+j)//2] == 'X': # 파티션 있을 경우
                                break
                        else:
                            return False
                    
                    else: # 다른 행인 경우
                        if r < i and j < c and places[r][j] == 'X' and places[i][c] == 'X':
                            break
                        if i < r and c < j and places[i][c] == 'X' and places[r][j] == 'X':
                            break
                        if i < r and j < c and places[r][j] == 'X' and places[i][c] == 'X':
                            break
                        if r < i and c < j and places[i][c] == 'X' and places[r][j] == 'X':
                            break  
                        else:
                            return False
    return True



def get_result(places):
    for j in range(5):
        for k in range(5):
            if places[j][k] == 'P': # 응시자일 경우
                if get_distance(places, j,k) == False:
                    answer.append(0)
                    return answer
                
    answer.append(1)
    return answer
                


global answer 
answer = []
for i in range(5):
    get_result(places[i])
print(answer)
    

        
        
                   
