'''

sam의 피자 학교


1. 밀가루 양이 가장 적은 위치에 밀가루를 1 만큼 더 넣어주기

- 여러 개 라면, 여러 개 다 넣어주기


2. 도우 말아주기

- 바닥에 있는 밀가루 보다 위에 있는 밀가루가 더 넗으면 중단

2차원 배열의 움직임을 1차원 배열로 기록하면 쉽다.

3. 도우를 꾹 눌러주기

동시에 => "temp 배열이 필요해, 동시에 진행 해야 함."

인접(상 하 좌 우)에 두 a, b => |a - b|를 5로 나누고

큰 곳에는 몫을 빼고, 작은 곳에는 몫을 더해준다.

3 - 1. 1줄로 변환 => 열이 작은 것 부터 나열, 열이 같다면 행이 작은 것 부터 나열 순서대로 좌측에

수학시간에 그래프를 그린다고 생각. 좌측 하단이 (0, 0)


4. 도우를 (두 번) 반 으로 접어 주기

종이 접는다고 생각! 잘라서 올리는 것이 아님!


5. 3의 과장만 한번 더 진행


1 ~ 5 과정을 1회 시뮬레이션

각 위치의 밀가루 향의 최댓값과 최솟값의 차이가 k 이하가 될 때까지 반복

k 이하가 되기 위한 최소 반복 횟수를 구하라

'''
# print([(0,0)] * 4)
# 리스트안의 튜플이 * 4 되네
# [(0, 0), (0, 0), (0, 0), (0, 0)]

# s_index = 2
# for i, (row, col) in enumerate([(0, 0), (0, 0), (0, 0), (0, 0)]):
#     s_index += 1
#
# print(s_index)

# 초기 입력

n, k = map(int, input().split())

MAP = list(map(int, input().split()))

#동시 처리 위한 임시 배열
new_MAP = [0] * n

#경과 시간
elapsed_time = 0


# 1 단계
def add_min_val_flour():
    #최솟값을 찾아 전부 1씩 더해주기
    min_val = min(MAP)

    for i in range(n):
        if MAP[i] == min_val:
            MAP[i] += 1

# (row_num, col_num)판을 기준으로
# 시계방향으로 90' 회전한 이후의 위치를 구합니다.
def rotate(flours, row_num, col_num):
    for i, (x, y) in enumerate(flours):
        flours[i] = (y, row_num - x + 1)
# 2 단계
def roll_up():

    # 말아올려진 후, 각 숫자들의 위치를 구한다.
    flours = [(0, 0)] * n

    # 처음 2개를 놓고 시작
    flours[0] = (1, 1)
    flours[1] = (2, 1)
    # row가 2개, col이 하나 인 것
    # 즉, 세로 한줄로 2개 층이 이룬 것 이미
    row_num, col_num = 2, 1

    #말아지는 좌표의 갯수들
    s_index = 2

    while s_index + row_num <= n:

        #기존 숫자들은 90도 회전
        for i, (row, col) in enumerate(flours):
            flours[i] = (col, row_num - row + 1)
        # rotate(flours, row_num, col_num)
        #새롭게 추가되는 숫자들의 위치를 잡아줌.
        for i in range(1, row_num + 1):
            flours[s_index] = (col_num + 1, i)
            s_index += 1
        #말아 올려진 이후의 row, col 개수를 갱신
        if row_num == col_num + 1:
            #옆으로 넓어질 떄는 이전에 row_num의 숫자가 더 많았을 때
            col_num += 1
        else:
            #row가 더 많아지는 때는 그 이전에 row_num col_num이 같을 때
            row_num += 1

    #남아 있는 부분의 위치를 계산
    delta = 1
    while s_index < n:
        flours[s_index] = (row_num, col_num + delta)
        s_index += 1
        delta += 1

    return flours

# 3 + 알파 단계
def re_arrange(flours):

    #temp를 초기화
    for i in range(n):
        new_MAP[i] = 0

    # 오 아래처럼 할 수도 있구나..
    # row, col은 sort의 기준이 되니깐 tuple에 저렇게 담고
    # index는 나중에 또 임시배열 new_MAP에 담을 떄 필요하니 꺼내고
    # 열 오름 차순, 행 내림차순이라 (col, - row, i) 이렇게 뽑은 것

    # 열은 오름차순, 행은 내림차순, temp에 넣기
    extended_flours = [(col, -row, i) for i, (row, col) in enumerate(flours)]

    #위에서 처럼 안했으면, 아래에서 조정을 했어야 했음. 람다를 사용해서
    extended_flours.sort()

    #사용하지 않아서 _로 한것. 원래는 "인덱스 , (row, col)"이지만!
    for i, (_, _, prev_index) in enumerate(extended_flours):
        new_MAP[i] = MAP[prev_index]

    #원래 MAP에 넣기
    for i in range(n):
        MAP[i] = new_MAP[i]

# 두 위치가 인접한 곳인지를 판단합니다.
def adjacency(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2) == 1
# 3단계
def press(flours):

    #temp 초기화. 전역으로 설정해서, 초기화 작업이 필요함.
    #왜냐면 여러곳에서 다시 MAP을 재 설정해야 한다.
    for i in range(n):
        #0으로 초기화 하는게 아니라, 새로운 MAP을 만들어서 "동시"를 구현
        new_MAP[i] = MAP[i]

    # 인접한 쌍끼리 밀가루 양을 서로 옮겨주기

    for i in range(n):
        for j in range(i + 1, n):
            #모든 위치에서 진행되고, 중복이 될 수 있다.
            (row1, col1) = flours[i]
            (row2, col2) = flours[j]

            # if adjacency(row1, col1, row2, col2):
            if abs(row1 - row2) + abs(col1 - col2) == 1 :
                if MAP[i] > MAP[j]:
                    new_MAP[i] -= (MAP[i] - MAP[j]) // 5
                    new_MAP[j] += (MAP[i] - MAP[j]) // 5

                else:
                    new_MAP[i] += (MAP[j] - MAP[i]) // 5
                    new_MAP[j] -= (MAP[j] - MAP[i]) // 5


    for i in range(n):
        MAP[i] = new_MAP[i]

    #펴주는 작업
    re_arrange(flours)

#4 단계

def fold():
    flours = [(0, 0)] * n
    # 한번 접은 후의 위치 구하기
    for i in range(n // 2):
        flours[i] = (1, n // 2 - i)
    for i in range(n // 2, n):
        flours[i] = (2, i - (n // 2) + 1)

    # 두번 접은 후의 위치 구하기
    for i, (x, y) in enumerate(flours):
        # 접었을 때 위로 올라가는 부분
        if y <= n // 4:
            flours[i] = (3 - x, n // 4 - y + 1)
        # 접었을 때 아래에 남아있는 부분
        else:
            flours[i] = (x + 2, y - n // 4)

    return flours


def simulate():
    global elapsed_time

    # Step 1. 가장 작은 숫자를 찾아 전부 1을 증가시켜줍니다.
    add_min_val_flour()

    # Step 2. 도우를 말아줍니다.
    flours = roll_up()

    # Step 3. 도우를 꾹 눌러줍니다.
    press(flours)

    # Step 4. 도우를 두 번 반으로 접어줍니다.
    flours = fold()

    # Step 5. 도우를 한번 더 꾹 눌러줍니다.
    press(flours)

    # 횟수를 증가시켜줍니다.
    elapsed_time += 1


def end():
    # 전부 차이가 k 이내인지 판단합니다.
    return max(MAP) - min(MAP) <= k


# 차이가 k보다 크다면 계속 반복합니다.
while not end():
    simulate()

print(elapsed_time)