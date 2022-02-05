'''
실전문제 4 - 1이 될 때까지
P. 99쪽 (그리디)
'''

N, K = map(int, input().split())
count = 0
while(N != 1):  
    if N % K ==0:
        N /= K
        count += 1
    else:
        N -=1
        count+=1
        
print(count)


