"""
-- 해설 공부 --
실패의 원인 : 너무 오래 붙잡았고 + 변수를 너무 안쓰려고 했다.
그냥 다 나눠서 저장하고, 그냥 다 매번 반영해주는게 훨씬 쉽고 빠른 것 같다.
하나의 2차원 배열 안에 꾸역꾸역 끼워넣으려고 하지 않아야겠다.

문제 전개를 위해 필요한 전역 변수는 다음과 같다.
1. board : 실제 보드 상황 그 자체
2. v : 각 팀별로 경로를 저장한다. 경로의 좌표를 tuple형태로 모두 list에 저장
3. tail : 각 팀별로 머리 + 몸통 + 꼬리의 수를 저장한 셈이다. 이 변수는 움직일때, 뒤집힐 때 1,2,3 과 4를 구분하기 위해 사용된다.
4. visited : 초반에 경로 만들때만 사용한다.
5. board_idx : 공을 맞은 경우 팀 정보를 알아야 그 팀의 방향을 뒤집을 수 있다.
6. dxs, dys : 북서남동

문제 전개를 위해 만든 함수는 다음과 같다.

1. init : board, v, tail, visited, board_idx 등 필요한 내용을 채우는 부분이다.
          v를 채울 때 각 팀의 머리부터 저장한다. 이후 각 팀의 머리를 기준으로 경로를 만들어간다.
2. dfs : v를 만드는 함수이다. x, y, idx(팀 번호)가 매개변수로 필요하다.
         visited 배열로 중복 방문을 방지하고, 방문할 때마다 board_idx 를 채워준다.
         is_out_range라는 함수를 작성해서 범위를 넘어갈 경우 처리해주었는데 매우 간결해서 맘에 든다.
         가장 처음 탐색할 때 몸통으로 움직이도록 유도한다. 2를 찾았다면 다음 2를 찾으러 가는데, 가다가 3이 나오면 tail 배열에 이제까지의
         머리 + 몸통 + 꼬리의 수를 저장해준다. return값은 아무것도 없다.
이제 각 라운드마다 실행되는 함수이다.
3. move_all : 각 팀을 이동시키는 함수다. 각 팀마다 레일을 뒤로 이동시킨다고 쓰여있는데, 머리는 마지막 4의 위치로 가면서 한칸씩 앞으로 가는 셈이다.
              0의 값을 1에, 1의 값을 2에, 2의 값을 3에 저장하면서 한칸 씩 앞으로 가게 되는 것이다. 마지막 4의 위치는 저장해놨다가 마지막에 머리에 넣는다.
              레일을 움직였으면 그에 맞춰 보드의 표기를 바꿔주어야 한다. 이때 enumerate를 써서 index 값으로 머리 / 몸통 / 꼬리 / 레일을 구분한다.
              참 편하다 ㅡㅡ
4. throw_ball : 공을 던진다. 현재 몇 번째 라운드인지 매개변수로 받는다. 상하좌우 구분을 위한 계산식이 좀 굳이? 싶다.
                쨌든 맞은 사람이 있으면 점수를 구하고, get_point를 통해 몇번째 팀인지 반환한다.
                나는 break로 멈췄는데 return으로 팀 정보를 반환하는게 더 좋아보인다.
5. get_point : 함수 자체는 매우 심플하다. 어디서 공을 맞았는지 좌표를 매개변수로 넘긴다.
               board_idx에서 무슨 팀인지 찾아내고, v[idx].index((x,y))를 통해 몇 번째 사람인지 찾아낸다.
               와.. 나는 이게 매우 막막하다고 생각했는데, 사실 엄청 막막한건 기본 함수로 쉽게 풀 수 있는 거였나 싶다.
               내가 막막했던 이유는 팀의 정보를 따로 저장하지 않아서 어느 팀인지 찾아내고, 그 팀의 몇번째 사람인지 일일이 찾으려고 했기 때문이다.
               못 할건 아니지만 너무 번거롭달까... 아무튼 여기서 점수를 반영하고 팀 정보를 반환한다.
6. reverse : 공을 맞은 팀은 방향을 뒤집어야한다. 어느 팀인지 매개변수로 받는다.
             나는 이걸 시계방향으로 구현하려고 했는데, 그럴 필요 없이 v를 생짜로 다 뒤집는다.
             새로운 루트를 저장할 new_v를 만들고, 1,2,3에 해당하는 좌표들을 우선 뒤에서부터 넣는다.
             그러면 3 - 2 - 1 순으로 앞에서부터 저장된다. 이건 루트이기 때문에 4도 저장해야한다.
             따라서 기존 루트에서 1,2,3 부분을 제외한 tail+1 ~ len(v) 범위의 좌표들을 뒤집어서 저장해준다.
             이렇게 뒤집힌 루트에 맞춰 board를 업데이트해주면 된다. board_idx는 바꿀 필요가 없다!

힘들다ㅠ
"""



# 변수 선언 및 입력:


n, m, k = tuple(map(int, input().split()))
board = [[0] * (n + 1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

# 각 팀별 레일 위치를 관리합니다.
v = [[] for _ in range(m + 1)]
# 각 팀별 tail 위치를 관리합니다.
tail = [0] * (m + 1)
visited = [
    [False] * (n + 1)
    for _ in range(n + 1)
]

# 격자 내 레일에 각 팀 번호를 적어줍니다.
board_idx = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

ans = 0

dxs = [-1,  0, 1, 0]
dys = [ 0, -1, 0, 1]


def is_out_range(x, y):
    return not (1 <= x and x <= n and 1 <= y and y <= n)


# 초기 레일을 만들기 위해 dfs를 이용합니다.
def dfs(x, y, idx):
    visited[x][y] = True
    board_idx[x][y] = idx
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_out_range(nx, ny):
            continue

        # 이미 지나간 경로거나 경로가 아니면 넘어갑니다.
        if board[nx][ny] == 0:
            continue
        if visited[nx][ny]:
            continue

        # 가장 처음 탐색할 때 2가 있는 방향으로 dfs를 진행합니다.
        if len(v[idx]) == 1 and board[nx][ny] != 2:
            continue

        v[idx].append((nx, ny))
        if board[nx][ny] == 3:
            tail[idx] = len(v[idx])
        dfs(nx, ny, idx)


# 초기 작업을 합니다.
def init():
    cnt = 1

    # 레일을 벡터에 저장합니다. 머리사람을 우선 앞에 넣어줍니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] == 1:
                v[cnt].append((i, j))
                cnt += 1

    # dfs를 통해 레일을 벡터에 순서대로 넣어줍니다.
    for i in range(1, m + 1):
        x, y = v[i][0]
        dfs(x, y, i)


# 각 팀을 이동시키는 함수입니다.
def move_all():
    for i in range(1, m + 1):
        # 각 팀에 대해 레일을 한 칸씩 뒤로 이동시킵니다.
        tmp = v[i][-1]
        for j in range(len(v[i]) - 1, 0, -1):
            v[i][j] = v[i][j - 1]
        v[i][0] = tmp

    for i in range(1, m + 1):
        # 벡터에 저장한 정보를 바탕으로 보드의 표기 역시 바꿔줍니다.
        for j, (x, y) in enumerate(v[i]):
            if j == 0:
                board[x][y] = 1
            elif j < tail[i] - 1:
                board[x][y] = 2
            elif j == tail[i] - 1:
                board[x][y] = 3
            else:
                board[x][y] = 4


# (x, y) 지점에 공이 닿았을 때의 점수를 계산합니다.
def get_point(x, y):
    global ans
    idx = board_idx[x][y]
    cnt = v[idx].index((x, y))
    ans += (cnt + 1) * (cnt + 1)


# turn 번째 라운드의 공을 던집니다.
# 공을 던졌을 때 이를 받은 팀의 번호를 반환합니다.
def throw_ball(turn):
    t = (turn - 1) % (4 * n) + 1

    if t <= n:
        # 1 ~ n 라운드의 경우 왼쪽에서 오른쪽 방향으로 공을 던집니다.
        for i in range(1, n + 1):
            if 1 <= board[t][i] and board[t][i] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(t, i)
                return board_idx[t][i]
    elif t <= 2 * n:
        # n+1 ~ 2n 라운드의 경우 아래에서 윗쪽 방향으로 공을 던집니다.
        t -= n
        for i in range(1, n + 1):
            if 1 <= board[n + 1 - i][t] and board[n + 1 - i][t] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(n + 1 - i, t)
                return board_idx[n + 1 - i][t]
    elif t <= 3 * n:
        # 2n+1 ~ 3n 라운드의 경우 오른쪽에서 왼쪽 방향으로 공을 던집니다.
        t -= (2 * n)
        for i in range(1, n + 1):
            if 1 <= board[n + 1 - t][n + 1 - i] and board[n + 1 - t][n + 1 - i] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(n + 1 - t, n + 1 - i)
                return board_idx[n + 1 - t][n + 1 - i]
    else:
        # 3n+1 ~ 4n 라운드의 경우 위에서 아랫쪽 방향으로 공을 던집니다.
        t -= (3 * n)
        for i in range(1, n + 1):
            if 1 <= board[i][n + 1 - t] and board[i][n + 1 - t] <= 3:
                # 사람이 있는 첫 번째 지점을 찾습니다.
                # 찾게 되면 점수를 체크한 뒤 찾은 사람의 팀 번호를 저장합니다.
                get_point(i, n + 1 - t)
                return board_idx[i][n + 1 - t]

    # 공이 그대로 지나간다면 0을 반환합니다.
    return 0


# 공을 획득한 팀을 순서를 바꿉니다.
def reverse(got_ball_idx):
    # 아무도 공을 받지 못했으면 넘어갑니다.
    if got_ball_idx == 0:
        return

    idx = got_ball_idx

    new_v = []

    # 순서를 맞춰 new_v에 레일을 넣어줍니다.
    for j in range(tail[idx] - 1, -1, -1):
        new_v.append(v[idx][j])

    for j in range(len(v[idx]) - 1, tail[idx] - 1, -1):
        new_v.append(v[idx][j])

    v[idx] = new_v[:]

    # 벡터에 저장한 정보를 바탕으로 보드의 표기 역시 바꿔줍니다.
    for j, (x, y) in enumerate(v[idx]):
        if j == 0:
            board[x][y] = 1
        elif j < tail[idx] - 1:
            board[x][y] = 2
        elif j == tail[idx] - 1:
            board[x][y] = 3
        else:
            board[x][y] = 4


# 입력을 받고 구현을 위한 기본적인 처리를 합니다.
init()
for i in range(1, k + 1):
# 각 팀을 머리사람을 따라 한칸씩 이동시킵니다.
    move_all()

    # i번째 라운드의 공을 던집니다. 공을 받은 사람을 찾아 점수를 추가합니다.
    got_ball_idx = throw_ball(i)

    # 공을 획득한 팀의 방향을 바꿉니다.
    reverse(got_ball_idx)

print(ans)