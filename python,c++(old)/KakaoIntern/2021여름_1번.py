# -*- coding: utf-8 -*-
"""
1번 3시 19분 솔 (55분 걸림)
"""

num_str = ['zero', 'one', 'two', 'three', 'four','five','six','seven','eight','nine']
ans = []



s = "oneseven4eightseven"
# 코드 참고 : https://pmandocom.tistory.com/17
def find_index(data, target):
  res = []
  lis = data
  while True:
    try:
      res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0)) #+1의 이유 : 0부터 시작이니까
      lis = data[res[-1]+1:]
    except:
      break     
  return res

for i in num_str:
    if find_index(s, i):
        idx = find_index(s, i)
        for j in idx:
            ans.append((j,i))
       
        
for i in range(len(s)):
    if s[i].isdigit():
        ans.append((i, s[i]))

print(ans)

ans.sort(key=lambda x:x[0])
print(ans)
temp_answer = []
for idx, val in ans:
    if val.isdigit():
        temp_answer.append(int(val))
    else:
        for i in range(len(num_str)):
            if val == num_str[i]:
                temp_answer.append(int(i))
                
                
print(temp_answer)
answer = 0
for i in range(0, len(temp_answer)):
    answer += temp_answer[i] * 10**(len(temp_answer) - i-1)
    
print(answer)
                

    
    
    