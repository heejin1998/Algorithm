n = int(input())
bag = 0
flag = True
while n > 0:

    if n % 5 == 0:
        n -= 5
        bag += 1
    else:
        n -= 3
        if n <0:
            print(-1)
            flag = False
            break
        bag += 1

if flag:
    print(bag)