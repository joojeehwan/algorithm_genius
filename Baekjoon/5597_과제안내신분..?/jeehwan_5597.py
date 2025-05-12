N = 30
arr = [0] * (N+1)

for i in range(28) :
    num = int(input())
    arr[num] = 1

for i in range(1,N+1):
    if arr[i] == 0:
        print(i)
