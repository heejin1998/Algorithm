# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:42:45 2021

@author: bobae
"""

N = int(input())
dir = list((input().split()))

loc_col = 1
loc_row = 1

for i in dir:
  if i == 'L':
    if loc_row != 1:
      print("L")
      loc_row -= 1
    else:
      continue
  elif i == 'R':
    if loc_row != N:
      print("R")
      loc_row += 1
    else:
      continue
  elif i == 'U':
    if loc_col != 1:
      print("U")
      loc_col -= 1
    else:
      continue
  else: #dir =='D'
    if loc_col != N :
      print("D")
      loc_col += 1
    else:
      continue

print(loc_col, loc_row)


