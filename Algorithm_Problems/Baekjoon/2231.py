n = int(input())
flag = 0
for i in range(n) :
    sumv = 0
    num = i
    while True :
        if num == 0 :
             break
        sumv += num%10
        num = num//10
    if sumv+i == n :
        print(i)
        flag = 1
        break
if flag == 0 :
    print(0)