import sys

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

di = [0, 1, 1]
dj = [1, 0, 1]
def check(now_i, now_j):
    global answer

    l = min(M-now_j, N-now_i)
    for x in range(l-1, 0, -1):
        flag = 1
        for k in range(3):                              # 오른쪽, 아래, 대각선 꼭짓점을 모두 검사해서
            next_i = now_i + di[k] * x
            next_j = now_j + dj[k] * x

            if MAP[next_i][next_j] != MAP[now_i][now_j]:
                flag = 0
                break
        if flag:                                        # 정사각형이 만들어지면 리턴
            return x

    return -1

answer = 0
for i in range(N-1):
    for j in range(M-1):                            # 어차피 맨 끝줄은 검사해봣자 최대 1이니까 그 전 행, 열까지 검사
        answer = max(answer, check(i, j))

print((answer + 1) ** 2)                            # 정답 +1의 제곱이 정사각형의 크기