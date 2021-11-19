zum=[]
x_list = []
y_list = []
for i in range(3):
    x, y= map(int,input().split())
    x_list.append(x)
    y_list.append(y)



for x in x_list:
    if x_list.count(x)==1:
        res_x = x

for y in y_list:
    if y_list.count(y)==1:
        res_y = y
print(res_x, res_y)