import sys
from copy import deepcopy

input = sys.stdin
# 떨어지는 블록의 수
n = int(input.readline())
# 통의 높이는 무제한이지만, 어차피 중력으로 인해 최대 n+1까지만 블록이 쌓일 수 있다.
m = n + 1

answer = 0

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# 블럭은 8개의 타입이 있고, 각 타입마다 이동 방향 우선순위를 저장해준다.
b_types = [[]]
# 블럭의 타입, 위치(col)을 저장해둔다.
blocks = []


# 그냥 2차원 배열 출력하는 함수 따로 만들어서 디버깅할때 씀
def bucket_info(dumm):
    print("~~~~~~ 지금 상태 ~~~~~~~~")
    for line in dumm:
        print(*line)


# 현재 블럭과, 위치
def game(bucket, now_score, b_idx, pos):
    global answer
    print(f"----{b_idx+1}번째 블럭 하나 {pos+1}로 내려가는 중 ----")
    # 테트리스 처럼 현재 열 중에 앉을 수 있는 행을 찾는다.
    row = m-1
    while bucket[row][pos]:
        row -= 1
    bucket[row][pos] = blocks[b_idx][0]

    # bucket_info(bucket)
    if b_idx > 2:
        # 블럭이 4개는 되어야 점수를 계산할 수 있을테니..
        now_score1 = check(bucket)
        # bucket_info(bucket)
        # 점수를 얻었다 = 빈 줄이 생겼다 = 중력을 줘야한다.
        if now_score1:
            now_score += now_score1
            gravity(bucket)
            # bucket_info(bucket)
    # 각자 이동방향에 따라 움직인다.
    move(bucket)
    # bucket_info(bucket)
    # 움직였으면 중력을 적용해야한다.
    gravity(bucket)
    # bucket_info(bucket)
    if b_idx > 2:
        # 역시나 또 점수를 받았는지 보고, 점수가 있다면 중력을 적용한다.
        now_score2 = check(bucket)
        if now_score2:
            now_score += now_score2
            gravity(bucket)

    # 다음 블럭
    b_idx += 1
    if b_idx == n:
        # 마지막 블럭까지 다 봤다면, 최고 점수를 갱신한다.
        answer = max(now_score, answer)
        # bucket_info(bucket)
        # print(f"%%%%%%%% 모든 블럭 다봄 지금 점수 : {now_score} & {answer} %%%%%%%%")
        return
    if blocks[b_idx][1]:
        # 다음 블럭이 내려갈 위치가 정해져있다.
        game(bucket, now_score, b_idx, blocks[b_idx][1]-1)
    else:
        for c in range(4):
            # 다음 블럭이 내려갈 위치가 정해져있지 않다.
            temp_bucket = deepcopy(bucket)
            # print(f"****** {b_idx+1}번째 블럭 이번엔 {c} 열로 가봅니다. ******** ")
            # print(f"****** {b_idx+1}번째 블럭 이번엔 {c} 열로 가봅니다. ******** ")
            game(temp_bucket, now_score, b_idx, c)


def check(bucket):
    # print("======= 점수 획득 가능한지 체크 =======")
    score = 0

    for row in range(m):
        if 0 not in bucket[row]:
            score += 1
            bucket[row] = [0, 0, 0, 0]
    # if not score:
    #     print("^^^^^^^^^^^^^^^ 어림도 없지! ^^^^^^^^^^^^^^")
    # else:
    #     print("vvvvvvvvvvvvvvv 올~ㅋ 성공! vvvvvvvvvvvvvvv")
    return score


def gravity(bucket):
    # print("====== 중력에 따라 내려가야됨 =======")
    # 이건 자주 나오는 부분인데, 막상 구현하려면 헤매게 된다.
    # 또 바닥부터 봐야하니까 처음에 블록 저장할 때 바닥부터 저장해야한다.
    # 이 문제는 통의 길이가 정해져있지 않았기 때문에 난감했다.
    # 이런 함정에 말리지 않기 위해 최대 높이가 n+1인걸 깨닫는게 중요한 것 같다.
    for col in range(4):
        empty = 0
        for row in range(m-1, -1, -1):
            # 비어있는 만큼 길이를 저장하고, 아닌 부분을 만나면 그때 복사해준다.
            if not bucket[row][col]:
                empty += 1
            else:
                bucket[row+empty][col] = bucket[row][col]
        # 그리고 빈 만큼 위에서부터 0으로 채운다.
        for row in range(empty):
            bucket[row][col] = 0


def move(bucket):
    # print("======== 우선 순위에 따라 이동 ========")
    # 같은 위치에 블럭이 2개 이상일 경우 때문에 dictionary를 썼는데,
    # 그냥 기존 위치에 블럭이 있으면 최소값을 저장해주면 될 일이었다.
    move_blocks = dict()

    for row in range(m):
        for col in range(4):
            if bucket[row][col]:
                block_type = bucket[row][col]
                priorities = b_types[block_type]
                for d in priorities:
                    new_row = row + dr[d]
                    new_col = col + dc[d]
                    if 0 <= new_row < m and 0 <= new_col < 4:
                        key = (new_row, new_col)
                        if move_blocks.get(key):
                            move_blocks[key].append(block_type)
                        else:
                            move_blocks[key] = [block_type]
                        break
                bucket[row][col] = 0

    for row, col in move_blocks.keys():
        now_type = min(move_blocks[(row, col)])
        bucket[row][col] = now_type


# 블럭은 8개의 타입이 있고, 각 타입마다 이동 방향 우선순위를 저장해준다.
for _ in range(8):
    b_types.append(list(map(int, input.readline().split())))

# 블럭의 타입, 위치(col)을 저장해둔다.
for _ in range(n):
    b_type, b_pos = map(int, input.readline().split())
    blocks.append((b_type, b_pos))


if blocks[0][1]:
    game([[0] * 4 for _ in range(m)], 0, 0, blocks[0][1]-1)
else:
    for i in range(4):
        # 정해지지 않았다면, 4개의 열을 차례대로 방문한다.
        print(f"****** 처음!! 이번엔 {i} 열로 가봅니다. ******** ")
        game([[0] * 4 for _ in range(m)], 0, 0, i)

print(answer)