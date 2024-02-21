n = int(input())
arr=list(map(int,input().split()))
b, c = map(int, input().split())

result=n

for i in range(n) :
    if arr[i] - b <= 0 :
        continue
    else :
        tmp=(arr[i]-b)/c
        if tmp != int(tmp) :
            tmp = int(tmp)+1
        result += tmp
print(int(result))
