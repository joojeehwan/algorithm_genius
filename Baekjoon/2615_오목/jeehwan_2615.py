



# 바둑판 입력받기

MAP = [list(map(int, input().split())) for _ in range(19)]

loc = 0

# 우상, 우, 우하, 하 4가지 방향 check
dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

for row in range(19):
    for col in range(19):

        if MAP[row][col] == 0:
            continue

        #방향 설정
        for k in range(4):
            cnt = 0
            #해당 방향으로 얼마만큼 이동할 것인가 => 오목체크
            for i in range(5):
                next_row = row + dr[k] * i
                next_col = col + dc[k] * i
    
                #범위 확인
                if 0 <= next_row < 19 and 0 <= next_col < 19 :
                    # cnt증가 시키기
                    if MAP[next_row][next_col] == MAP[row][col]:
                        cnt += 1

            #육목체크 알고리즘 => 시작의 반댓 방향과 마지막의 다음방향으로 같은 돌이 1개라도 있으면 육목이 되어버린다.
            next_row = row - dr[k]
            next_col = col - dc[k]

            if  0 <= next_row < 19 and 0 <= next_col < 19 and MAP[row][col] == MAP[next_row][next_col]:
                continue

            #그 이후 방향으로 하나라도 더 있으면 안됌.
            next_row = row + dr[k] * 5
            next_col = col + dc[k] * 5

            if 0 <= next_row < 19 and 0 <= next_col < 19 and MAP[row][col] == MAP[next_row][next_col]:
                continue

            #육목 체크 후에도 돌이 5개라면, 즉 5목이라면
            if cnt == 5:
                answer_row = row
                answer_col = col
                loc = MAP[row][col]
print(loc)
if loc != 0:
    print(answer_row + 1, answer_col + 1)
