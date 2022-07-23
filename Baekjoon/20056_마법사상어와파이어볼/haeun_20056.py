"""
시간 524ms 메모리 32884 KB
푸는데 걸린 시간 90분

"""

import sys

N, M, K = map(int, sys.stdin.readline().split())
fireballs = dict()

# 방향 배열
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 파이어볼을 위치(r, c)를 key로 딕셔너리에 저장
for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    # 1과 N은 이어져있다는데, 나는 0부터 위치 처리할 거라서 1씩 다 뺌
    r -= 1
    c -= 1

    if fireballs.get((r, c)):
        fireballs[(r, c)].append((m, s, d))
    else:
        fireballs[(r, c)] = [(m, s, d)]


# print("------ 초기 -------")
# print(fireballs)

# 명령을 내린 횟수만큼 진행
for _ in range(K):

    # print(f"{_+1} 번째")

    # 이동한 파이어볼 정보로 나중에 업데이트
    # 반복문을 도는 와중에 변경이 되면 안되기 때문에
    moved_fireballs = dict()

    for row, col in fireballs:
        # 한 위치에 파이어볼이 여러개일 수 있기 때문에
        fires = fireballs[(row, col)]

        for m, s, d in fires:
            # 새로운 위치, 처음과 끝은 이어져있다고 한다.
            new_row = (row + s * dr[d]) % N
            new_col = (col + s * dc[d]) % N
            # 이미 그 위치에 있으면 더 추가하고, 아니면 새로 추가한다.
            if moved_fireballs.get((new_row, new_col)):
                moved_fireballs[(new_row, new_col)].append((m, s, d))
            else:
                moved_fireballs[(new_row, new_col)] = [(m, s, d)]

    # print("--- 움직임 -------")
    # print(moved_fireballs)

    # 파이어볼을 다 움직였다면
    for pos in moved_fireballs:
        # 한 위치에 파이어볼이 2개 이상이라면
        count = len(moved_fireballs[pos])

        if count > 1:
            sum_m, sum_s, sum_d = 0, 0, 0

            # 방향이 모두 홀,짝인지 보기 위한 Flag 변수
            same_sign = True

            # 제일 처음 파이어볼의 방향에 따라 뒤에 체크
            if moved_fireballs[pos][0][2] % 2:
                prev_dir_odd = True
            else:
                prev_dir_odd = False

            # 해당 위치에 있는 모든 파이어볼의 질량, 속도더하기
            for m, s, d in moved_fireballs[pos]:
                sum_m += m
                sum_s += s
                # 방향이 모두 홀수인지 짝수인지 판별해야한다.
                # 지금은 홀수인데 처음엔 짝수였던 경우 or 지금 짝수인데 처음엔 홀수였던 경우
                if (d % 2 and not prev_dir_odd) or (d % 2 == 0 and prev_dir_odd):
                    same_sign = False

            # 일단 기존에 있던 파이어볼은 비워준다.
            moved_fireballs[pos] = []

            # 다 더했다면 규칙대로 나누기
            # 나눈 질량이 1이 되지 않으면 그 위치에 다시 파이어볼을 만들 이유가 없다.
            if sum_m // 5 > 0:
                # 파이어볼은 4개의 파이어볼로 나누어진다.
                for i in range(4):
                    if same_sign:
                        moved_fireballs[pos].append((sum_m // 5, sum_s // count, i * 2))
                    else:
                        moved_fireballs[pos].append((sum_m // 5, sum_s // count, i * 2 + 1))

    # 업데이트
    fireballs = moved_fireballs

    # print("------합치기 끝남------")
    # print(fireballs)

answer = 0

# 모든 파이어볼의 질량 더하기
for pos in fireballs:
    for fire in fireballs[pos]:
        answer += fire[0]

print(answer)