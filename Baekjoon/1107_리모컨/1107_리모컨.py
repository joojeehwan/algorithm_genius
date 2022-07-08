N = int(input())
M = int(input())
if M:
    buttons = list(input().split())
else:
    buttons = []

cnt = abs(100-N)
for i in range(1000000 + 1):
    num = str(i)

    flag = 1
    for j in range(len(num)):
        if num[j] in buttons:
            flag = 0
            break

    if flag:
        cnt = min(cnt, abs(int(num) - N) + len(num))

print(cnt)

"""
완전탐색!!
0부터 마지막 번호까지 살펴보자
500000 까지니까 500000이 될 수 있는 1000000까지 살피면서
누를 수 있는 번호면 계산
"""
