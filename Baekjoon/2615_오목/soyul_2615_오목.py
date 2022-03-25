import sys

def check(now_i, now_j, num):

    for k in range(4):
        flag = 1
        for i in range(1, 5):                        # 앞으로 4개의 돌이 나와 같은지 검사
            next_i = now_i + di[k] * i
            next_j = now_j + dj[k] * i

            # 범위를 넘어가거나 다른 돌이면 더 검사 X
            if next_i < 0 or next_j < 0 or next_i >= 19 or next_j >= 19:
                flag = 0
                break
            if MAP[next_i][next_j] != num:
                flag = 0
                break
        if flag:                                    # 5개의 돌이 이어졌다면 6목 검사
            # 앞으로 확인
            if next_i + di[k] >= 0 and next_i + di[k] < 19 and next_j + dj[k] >= 0 and next_j + dj[k] < 19:
                if MAP[next_i + di[k]][next_j + dj[k]] == num:
                    flag = 0
            # 뒤로 확인
            if now_i - di[k] >= 0 and now_i - di[k] < 19 and now_j - dj[k] >= 0 and now_j - dj[k] < 19:
                if MAP[now_i - di[k]][now_j - dj[k]] == num:
                    flag = 0
            # 6목검사까지 끝나면
            if flag:
                return 1
    return flag

MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

di = [0, 1, 1, -1]             # 오른쪽 아래 오른쪽아래 오른쪽위
dj = [1, 0, 1, 1]

flag = 0
for i in range(19):
    if flag:
        break
    for j in range(19):
        if MAP[i][j] != 0:
            flag = check(i, j, MAP[i][j])
            if flag == 1:
                print(MAP[i][j])
                print(i+1, j+1)
                break
if not flag:
    print(0)