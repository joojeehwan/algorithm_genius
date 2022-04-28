"""
92ms 32572kb
주사위 회전하는 index 계산하면 되는건데
잘 해놓고 한두개 틀려서 디버깅하느라 시간 겁나 뺏김~!~!~!~!
"""
from collections import deque

answer = 0
N, M, K = map(int, input().split()) # 세로, 가로, 이동횟수
board = list(list(map(int, input().split())) for _ in range(N))

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 주사위 회전 / 북동남서 상하좌우 / 여기 처음에 실수해서 계산 오래걸림...
roll = [
    [1, 4, 0, 3, 0, 4],
    [2, 0, 3, 0, 2, 5],
    [3, 5, 0, 2, 0, 2],
    [4, 0, 4, 0, 1, 3], # 여기 마지막 2를 추가해서 배열이 이상해짐... 하ㅠㅠ내 시간~!
]


# 지도마다 점수 저장해두기
scores = [[0]*M for _ in range(N)]

# 점수 구할 때 쓸 방문 배열
visited = [[0]*M for _ in range(N)]


def set_score(row, col, num):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = 1
    count = 1
    same_scores = [(row, col)]

    while queue:
        now = queue.popleft()
        now_r, now_c = now[0], now[1]

        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            if 0 <= next_r < N and 0 <= next_c < M:
                if not visited[next_r][next_c] and board[next_r][next_c] == num:
                    visited[next_r][next_c] = 1
                    count += 1
                    queue.append((next_r, next_c))
                    same_scores.append((next_r, next_c))

    # 같은 점수를 가지고 상하좌우로 이동할 수 있는 곳 끼리 기록하기
    for r, c in same_scores:
        scores[r][c] = count * num


# 지도마다 점수 구하기
for row in range(N):
    for col in range(M):
        if not visited[row][col]:
            set_score(row, col, board[row][col])

# for line in scores:
#     print(*line)

# 주사위 굴려서 점수 찾기
dice = [1, 2, 3, 5, 4, 6]
dice_dir = 1 # 북동남서라서 index 번호 1
dice_row, dice_col = 0, 0

for turn in range(K):
    # print(f"지금 방향 : {dice_dir}")
    # 위치 이동
    if not (0 <= dice_row + dr[dice_dir] < N and 0 <= dice_col + dc[dice_dir] < M):
        # 범위를 넘어가면 방향 바꾸기
        dice_dir = (dice_dir + 2) % 4
        # print(f"방향 반대로~! {dice_dir}")
    dice_row += dr[dice_dir]
    dice_col += dc[dice_dir]
    # print(f"이동한 곳 : {dice_row}, {dice_col}")

    # 주사위 굴리기
    rolled_dice = [0] * 6
    for idx in range(6):
        # print(f"새 인덱스: {(idx + roll[dice_dir][idx]) % 6} VS 원래 {idx}")
        new_idx = idx + roll[dice_dir][idx]
        rolled_dice[new_idx % 6] = dice[idx]

    # print(f"바뀐 주사위 모습 : {rolled_dice}")

    # 바닥과 비교
    number = board[dice_row][dice_col]
    bottom = rolled_dice[5]

    # print(f"주사위 {bottom} VS 바닥 {number}")

    if bottom > number:
        dice_dir = (dice_dir + 1) % 4
        # print("시계방향이야!!")
    elif bottom < number:
        dice_dir = (dice_dir + 3) % 4

    answer += scores[dice_row][dice_col]
    # print(f"{turn}번째 누적 점수 : {answer}")
    dice = rolled_dice

print(answer)
