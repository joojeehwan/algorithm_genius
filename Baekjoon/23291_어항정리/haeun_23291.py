from collections import deque
from copy import deepcopy

N, K = map(int, input().split())
input_fish = list(map(int, input().split()))
max_fish, min_fish = max(input_fish), min(input_fish)
# 2차원 배열을 사용하되, 미리 만들어두지 않고 사용한다.
# 한줄이 더 생긴다면 list 안에 새로운 list를 추가하는 식으로 진행한다.
bowls = deque()
bowls.append(deque(input_fish))
answer = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def print_bowls():
    print("########### 어항 출력 ##########")
    for i in range(len(bowls)):
        print(i, "번 : ", bowls[i])


def rotate(_bowls):
    # 이미 맨 왼쪽의 한개는 떼어서 위로 올린 상태로 왔음.
    r_bowl = deepcopy(_bowls)
    bowl_h = 2
    # 공중부양 블럭의 가로, 맨 밑줄의 가로
    float_width, bottom_width = 2, len(r_bowl[bowl_h-1])

    while float_width <= bottom_width:
        # 공중부양된 어항 저장할 곳
        floated = deque()

        # 한줄씩 보면서, top_len(너비) 만큼씩 떼어 저장한다. 회전시키려고
        pop_width = len(r_bowl[0])
        for row in range(bowl_h):
            line = []
            for _ in range(pop_width):
                line.append(r_bowl[row].popleft())
            floated.append(line)

        # 왼쪽을 떼다가 빈 줄이 생겼으면 제거한다.
        for row in range(bowl_h-1, -1, -1):
            if not r_bowl[row]:
                r_bowl.remove(r_bowl[row])

        # 회전 할 것이다.
        row, col = len(floated), len(floated[0])

        if row == col:
            # 정사각형이면 공식대로 회전시켜주면 된다.
            rotated = [[0] * col for _ in range(row)]
            for r in range(row):
                for c in range(col):
                    rotated[c][row-r-1] = floated[r][c]
        else:
            # 직사각형이면 row, col 길이를 뒤바꿔서 저장해야한다.
            rotated = [[0] * row for _ in range(col)]

            for c in range(col):
                for r in range(row-1, -1, -1):
                    rotated[c][row-r-1] = floated[r][c]

        # 회전한 결과를 어항에 역순으로 왼쪽(앞)에 추가한다.
        for i in range(col-1, -1, -1):
            r_bowl.appendleft(deque(rotated[i]))

        # 변수 값을 업데이트 해준다.
        bowl_h = len(r_bowl)
        float_width, bottom_width = len(r_bowl), len(r_bowl[bowl_h - 1]) - row

    return r_bowl


def balancing(_bowls):
    height = len(_bowls)
    # 나중에 더해줄 변동 값
    diff = [0] * height
    # 계산 했는지 확인 배열
    check = [0] * height
    # 행마다 열의 수가 달라서 이렇게 만들었다.
    for r in range(len(bowls)):
        diff[r] = [0] * len(_bowls[r])
        check[r] = [0] * len(_bowls[r])

    for r in range(height):
        # 행마다 열의 수가 다르다.
        col = len(_bowls[r])
        for c in range(col):
            now_num = _bowls[r][c]
            for delta in range(4):
                next_r, next_c = r + dr[delta], c + dc[delta]
                # 범위 넘어가는 거 체크마저 어렵네
                if not (0 <= next_r < height and 0 <= next_c < col):
                    continue
                # 윗줄이 현재 줄보다 col 수가 적으면 찾을 수 없다.
                if len(_bowls[next_r]) <= next_c:
                    continue
                if check[next_r][next_c]:
                    continue
                next_num = _bowls[next_r][next_c]
                differ = now_num - next_num
                d = abs(differ) // 5
                if d:
                    if differ > 0:
                        # 옆이 작다
                        diff[next_r][next_c] += d
                        diff[r][c] -= d
                    else:
                        # 내가 작다
                        diff[next_r][next_c] -= d
                        diff[r][c] += d
            # 중복 체크 안하게끔
            check[r][c] = 1

    result = deepcopy(_bowls)
    for r in range(height):
        # 행마다 열의 수가 다르다.
        col = len(_bowls[r])
        for c in range(col):
            result[r][c] += diff[r][c]
    return result


def flatten(_bowls):
    f_bowl = deepcopy(_bowls)
    flat = deque()

    while f_bowl:
        for r in range(len(f_bowl)-1, -1, -1):
            flat.append(f_bowl[r].popleft())
            if not f_bowl[r]:
                f_bowl.remove(f_bowl[r])

    return flat


# ---- 시작 ! -----
while max_fish - min_fish > K:

    # 1. 가장 적은 물고기를 가진 어항에 한마리씩 추가한다.
    # 일렬로 되어있다는건 bowls의 가장 첫번째 줄을 의미한다. 어차피 지금 한줄밖에 없음
    for i in range(N):
        if bowls[0][i] == min_fish:
            bowls[0][i] += 1

    # 2. 어항 쌓기 (가장 왼쪽 어항을 빼서 리스트에 넣고 그걸 bowls에 추가함)
    left_bowl = bowls[0].popleft()
    # pop(0)랑 deque 중에 뭐가 나을까.. -> deque로 선택
    bowls.appendleft(deque([left_bowl]))


    # 3. 2개 이상 쌓여있는 어항을 시계방향 90도 회전
    # 이후 두번째 줄에 다시 append
    # 맨 밑줄이 공중부양한 어항보다 짧으면 stop
    # 여기가 가장 어려운 부분임
    bowls = rotate(bowls)

    # 4. 물고기 수 차이에 따라 조절한다. 이따 7번에서 또 한다.
    bowls = balancing(bowls)

    # 5. 일렬로 배치한다.
    bowls = deque([flatten(bowls)])

    # 6. 두번, N / 2개씩 나눠서 180도 회전하고 붙인다.
    half = N // 2
    for _ in range(2):
        new_bowl = deque()
        height = len(bowls)
        for h in range(height-1, -1, -1):
            line = bowls[h]
            # 왼쪽 채우기
            left = deque()
            for i in range(half):
                left.append(line[i])
            left.reverse()
            new_bowl.append(left)

        for h in range(height):
            line = bowls[h]
            # 오른쪽 채우기
            right = deque()
            for i in range(half):
                right.append(line[half+i])
            new_bowl.append(right)
        bowls = deepcopy(new_bowl)
        half //= 2

    # 7. 물고기 조절 작업을 수행한다.
    bowls = balancing(bowls)
    # 8. 일렬로 변환한다.
    bowls = deque([flatten(bowls)])
    # 9. 최대 물고기 수와 최소 물고기 수를 업데이트한다.
    max_fish, min_fish = max(bowls[0]), min(bowls[0])
    # 10. 걸린 시간을 추가한다.
    answer += 1

print(answer)