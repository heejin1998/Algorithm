
def possible(answer):
    for x, y, obj in answer:
        if obj == 1: # 보
            if [x, y-1,0] in answer or [x+1, y-1, 0] in answer: # 한쪽 끝 부분이 기둥 위
                continue
            if [x-1, y, 1] in answer and [x+1, y, 1] in answer: # 양쪽 끝 부분이 다른 보와 동시에 연결
                continue
            return False # 아니면 false 반환
        elif obj == 0: # 기둥
            if y == 0: # 바닥 위
                continue
            if [x, y, 1] in answer or [x-1, y, 1] in answer: # 보의 한쪽 끝 부분
                continue
            if [x, y-1, 0] in answer: # 아래에 기둥 있을 때
                continue
            return False
    return True



def solution(n, build_frame):
    answer = [[]]
    for frame in build_frame:
        x, y, obj, operate = frame
        if operate == 1: # 설치
            answer.append([x, y, obj])
            if not possible(answer):
                answer.remove([x, y, obj])
           

        if operate == 0: # 삭제
            answer.remove([x, y, obj])
            if not possible(answer):
                answer.append([x, y, obj])                    
        answer.sort()
    return answer