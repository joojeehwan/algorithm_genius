'''

2022 어려움 술래잡기

'''

#초기 입력
n, m, h, k = map(int, input().split())

# 각 칸에 있는 도망자 정보를 관리 => 도망자의 방향만 저장하면 충분
# 이차원 배열의 값이 배열인 경우는 이렇게 해야 함.
hiders = [[[] for _ in range(n)] for _ in range(n)]

# temp 배열 hiders 배열을 동시에 이동 시키기 위한 temp 배열
next_hiders = [[[] for _ in range(n)] for _ in range(n)]

tree = [[False] * n for _ in range(n)]

#정방향 기준으로 현재 위치에서 술래가 움직여야할 방향을 관리

seeker_next_dir = [[0] * n for _ in range(n)]

#역방향 기준으로 현재 위치에서 술래가 움직여야할 방향을 관리

seeker_rev_dir = [[0] * n for _ in range(n)]

#현재 위치 술래

seeker_pos = (n // 2, n // 2)

#술래 움직임 정방향 True, 역방향 False
forward_facing = True

#상 우 하 좌 (순서 이렇게)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 좌우하상 순서대로
h_dr = [0, 0, 1, -1]
h_dc = [-1, 1, 0, 0]

ans = 0

#도망자 정보 입력
for _ in range(m):

    row, col, dir = map(int, input().split())
    hiders[row - 1][col - 1].append(dir)


#나무 정보 입력
for _ in range(h):

    row, col = map(int, input().split())
    tree[row - 1][col - 1] = True


# 정중앙으로부터 (0,0) 까지 움직이는 술래의 경로를 계산
# 이건 내가 예전에 구현한 visited 배열로 하는게 아니라, 
# 2개씩 잘라서 늘려가는 방법


# 2개씩 잘러서 본것. 
def initialize_seeker_path():

    # 시작 위치와 방향
    # 해당 방향으로 이동할 수를 설정

    now_row, now_col = n // 2, n // 2
    move_dir, move_num = 0, 1

    debug = 1
    #둘 중 하나라도 참이면 가능...! 즉
    # 즉 둘다 0, 0 일때만, 거짓이 나와서 반복이 종료.
    while now_row or now_col:

        # 1 : 0,
        # 2 : 0 , 1
        for _ in range(move_num):
            seeker_next_dir[now_row][now_col] = move_dir

            now_row = now_row + dr[move_dir]
            now_col = now_col + dc[move_dir]

            # move_dir이 음수가 안나오도록 하기 위함
            # 모둘려 연산을 하는게 아니고, 아래에선 값을 넣는 경우 니깐!
            # 정방향으로 이동을 하면서, 동시에 같이 역방향도 같이 계산을 하는 구나.
            if move_dir < 2 :  #0, 1, 2, 3
                seeker_rev_dir[now_row][now_col] = move_dir + 2
            else:
                seeker_rev_dir[now_row][now_col] = move_dir - 2

            #(0, 0) 오게 되면 멈추기
            if not now_row and not now_col:
                break

        #방향 바꾸기
        move_dir = (move_dir + 1) % 4

        # 위, 아래가 될 떄 1씩 증가하면서 더 가야 한다.
        if move_dir == 0 or move_dir == 2:
            move_num += 1



#vistied 배열
'''

def solve(row, col):

    answer = 0
    visited = [[False] * n for _ in range(n)]
    dir = -1 #아무 방향 x, 방향은 0 ~ 4에 적용 되어 있음.
    while True :
        #(0,0)에 도착 => 토네이도의 이동을 멈춘다.
        if row == 0 and col == 0:
            break
        visited[row][col] = True
        next_dir = (dir + 1) % 4
        next_row = row + dr[next_dir]
        next_col = col + dc[next_dir]

        if visited[next_row][next_col] :
            #가려는 곳을 이미, 방문했기에 나선형을 만족하기 위해서, 다음 방향이 아닌, 이곳에 왓을때의 방향으로 다시
            next_dir = dir
            next_row = row + dr[next_dir]
            next_col = col + dc[next_dir]

        answer += movingSand(next_row, next_col, next_dir)
        #여기서 dir이 바뀌게 되고...
        row, col, dir = next_row, next_col, next_dir

    return answer

'''

def hider_move(row, col, move_dir):

    next_row, next_col = row + h_dr[move_dir], col + h_dc[move_dir]

    # step 1 격자를 벗어난다면, 우선 방향 틀어주기
    # 좌우 , 방향을 나눠서, 아래와 같이 해서, 그 나눈 곳 기준으로만 이동할 수 있도록
    if not (0 <= next_row < n and 0 <= next_col < n) :

        if move_dir < 2 :
            move_dir = 1 - move_dir
        else :
            move_dir = 5 - move_dir

        next_row = row + h_dr[move_dir]
        next_col = col + h_dc[move_dir]

    # 그런 다음에 그 위치에 술래가 없으며 움직이기.
    # hiders에는 초기 입려만 담기고, 이후에는 그냥 그대로 두고! 
    # 나는 항상 MAP을 만들면 그 안에서, 다 해결하려 했는데
    # 메모리를 더 사용하더라도, 위와 같이 만들어서(ex, next_hiders) 확실히 구분해서 하자.
    if (next_row, next_col) != seeker_pos :
        next_hiders[next_row][next_col].append(move_dir)
    #술래가 있으면 더 움직이지 X
    else:
        next_hiders[row][col].append(move_dir)


# def dist_from_seeker(x, y):
#     # 현재 술래의 위치를 불러옵니다.
#     seeker_x, seeker_y = seeker_pos
#     return abs(seeker_x - x) + abs(seeker_y - y)

def hider_move_all():

    #step 1. next_hirder를 초기화
    for row in range(n):
        for col in range(n):
            next_hiders[row][col] = []

    # step 2 전부 움직이기
    for row in range(n):
        for col in range(n):

            seeker_x, seeker_y = seeker_pos
            if abs(seeker_x - row) + abs(seeker_y - col) <= 3:
            # 거리가 3 이내인 도망자들에 대해서만 움직임
            # if dist_from_seeker(row, col) <= 3:
                #현재 hiders 들의 방향을 가지고 있음
                for move_dir in hiders[row][col] : 
                    hider_move(row, col, move_dir)
            # 그렇지 않다면, 현재 위치 그대로 넣어준다.
            else:
                for move_dir in hiders[row][col]:
                    next_hiders[row][col].append(move_dir)

    # step 3. next_hider의 값을 옮겨준다. "동시를 구현"

    for row in range(n):
        for col in range(n):
            hiders[row][col] = next_hiders[row][col]


# 현재 술래가 바라보는 방향을 가져옵니다.
def get_seeker_dir():
    # 현재 술래의 위치를 불러옵니다.
    x, y = seeker_pos

    # 어느 방향으로 움직여야 하는지에 대한 정보를 가져옵니다.

    if forward_facing:
        move_dir = seeker_next_dir[x][y]
    else:
        move_dir = seeker_rev_dir[x][y]

    return move_dir

def seeker_move():

    global seeker_pos, forward_facing

    row, col = seeker_pos

    move_dir = get_seeker_dir()

    #술래 한칸 움직이기
    seeker_pos = (row + dr[move_dir], col + dc[move_dir])
    
    # 끝에 도달하면 방향 바꿔주기

    #정방향으로 끝에 다다른 경우라면, 방향을 바꿔주기
    if seeker_pos == (0, 0) and forward_facing:
        forward_facing = False

    if seeker_pos == (n // 2, n // 2) and not forward_facing :
        forward_facing = True



def get_score(trun):

    global ans

    #현재 술래의 위치
    row, col = seeker_pos

    move_dir = get_seeker_dir()

    # 술래는 3칸 범위 안에 있는 도망자들만 체크 가능
    # 이런식으로 3번 곱하기 쌉가능
    for dist in range(3):
        next_row = row + dist * dr[move_dir]
        next_col = col + dist * dc[move_dir]

        #격자를 벗어나지 않으면서!, 나무가 없는 놈

        if 0 <= next_row < n and 0 <= next_col < n and not tree[next_row][next_col] :

            ans += trun * len(hiders[next_row][next_col])
            #도망자 사라짐
            hiders[next_row][next_col] = []


initialize_seeker_path()

for trun in range(1, k + 1):

    hider_move_all()

    seeker_move()

    get_score(trun)

print(ans)

        

