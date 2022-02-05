''' 
전형적인 시뮬레이션 문제

해당 문제는 구현 과정이 복잡하기 때문에, 무조건 코드로 옮기려고 하면 제대로 구현하기 어려워 오답 판정 가능

문제 해결을 쉽게 할 아이디어 정리 뒤 코드 작성 시작 

전체 명령 개수는 1,000개 이하. 전체 명령 개수를 M개라 설정하면 시간 복잡도 O(M^2)이 이상적
하지만 시간 제한이 5초로 넉넉한 편이므로 O(M^3)까지 괜찮다.
설치 및 삭제 연산을 요구할 때마다 일일이 '전체 구조물을 확인하며' 규칙을 확인하는 것
'''

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False 
        return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 최대 개수는 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과 반환 
