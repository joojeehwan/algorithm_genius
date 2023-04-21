"""
# 시작) 4:43 / 끝) 6:16 => 왜 시간을 줄이질 못 하니 왜!!
[문제 설명]
- N * N 격자 안에서 진행  2 <= N <= 20
    - 각각의 격자에는 무기가 '여러개' 있을 수 있다.
    - 초기에는 무기가 없는 빈 격자에 플레이어들이 위치
- 각 플레이어는 다음과 같은 정보를 지닌다. 1 <= M <= 30(최대)
    1. 초기 능력치 (모두 다름)
    2. 번호
    3. 방향
    4. 점수
    5. 위치 좌표 (r, c)
- 오른쪽 90도 회전 (상-우-하-좌)에 맞는 델타 배열 필요(입력 형식에 명시되어있음)
[정답]
- 각각 플레이어들이 획득한 점수를 스페이스를 포함해 한 줄에 출력한다.
"""
import sys
sys.stdin = open('input.txt', 'r')


# 입력 변수
N, M, K = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))

# 총 저장 => 3차원 배열. 한 위치에 총이 여러개 있을 수 있다.
guns = [[[] for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        guns[r][c].append(grid[r][c])

# 플레이어 변수
x, y = [0] * M, [0] * M  # 행, 열
d, s, g = [0] * M, [0] * M, [0] * M  # 방향, 초기 능력치, 소지한 총 공격력
point = [0] * M  # 점수

for i in range(M):
    _x, _y, _d, _s = map(int, input().split())  # 입력값 1부터 시작하는거 조심^^...
    x[i], y[i], d[i], s[i] = _x-1, _y-1, _d, _s

# 그 외 전역 변수
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]


# 출력 함수
def print_players():
    for i in range(M):
        print(f"{i} 번째 => 위치 : {x[i], y[i]} | 방향 : {d[i]} | 능력 : {s[i]} | 총 : {g[i]}")
    print(f"총 점수 {point}")
    print()


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


# - 본인이 향하는 방향대로 '한 칸' 만큼 이동
# - 격자를 벗어나면 정반대 방향으로 '한 칸' 만큼 이동
def move(p):
    px, py = x[p], y[p]
    pd = d[p]

    # [이런실수하지말라고🤬] dr을 왜 두번 쓰는데
    if not in_range(px + dr[pd], py + dc[pd]):
        d[p] = (pd+2) % 4  # 반대방향
        # [이런실수하지말라고🤬] 왜 방향 업데이트만 하고 반환하는건 그대로 했는데
        pd = d[p]

    return px + dr[pd], py + dc[pd]


def find_player(r, c):
    for other in range(M):
        # 가고 싶은 위치를 정한 플레이어는 아직 움직이지 않았다.
        # 그래서 어차피 그 위치가 아니니깐 본인인지 확인 안해도 된다.
        # [이런실수하지말라고🤬] 아니다.. 지고 다시 원래 있던 자리로 돌아가야할 때가 있다..
        # [이런실수하지말라고🤬] 와..^^ 이긴애도 아직 안움직여서.. 미치겠네^^
        # M의 최대값은 30이고, 이 함수는 최대 30*30*500 이므로 시간내 가능
        if x[other] == r and y[other] == c:
            return other
    return -1  # 아무도 없으면 -1 반환


# [총 획득]
# - 플레이어의 총을 격자에 내려둔다.
# - 가장 쎈 총을 획득한다.
def check_gun(p):
    r, c = x[p], y[p]
    # 플레이어가 총을 갖고 있다면 전체 비교를 위해 내려놓는다.
    if g[p]:
        guns[r][c].append(g[p])

    # [이런실수하지말라고🤬] 총이 없으면 max() 함수에서 ValueError 발생
    if guns[r][c]:
        # 가장 쎈 총을 찾는다.
        strongest = max(guns[r][c])
        # 가장 쎈 총을 플레이어에게 준다.
        g[p] = strongest
        # 플레이어에게 줬으니깐 현재 위치에 그 총은 더 이상 없다.
        guns[r][c].remove(strongest)


# (초기 능력치 + 총의 공격력)를 각각 비교한다.
#  - 같을 경우 초기 능력치가 높은 플레이어가 이긴다.
#  - 이긴 플레이어는 공격력 합의 차이만큼 포인트를 획득한다. (점수 기록 필요)
def fight(p1, p2):
    p1_attack = s[p1] + g[p1]
    p2_attack = s[p2] + g[p2]
    diff = abs(p1_attack - p2_attack)

    if p1_attack > p2_attack:
        return p1, p2, diff
    elif p1_attack < p2_attack:
        return p2, p1, diff
    else:
        if s[p1] > s[p2]:
            return p1, p2, diff
        else:
            return p2, p1, diff


#   - 자신의 총을 해당 격자에 내려놓고, 원래 방향대로 이동한다.
#   - 이때 이동하려는 칸에
#       1. 플레이어가 있거나 2. 격자 밖인 경우 -> 오른쪽으로 90도씩 회전하여 빈칸 찾아 이동
#           - 이에 맞춰 델타 배열 만들자.
#   - 이동한 뒤, [총 획득]
#       -> 해당 칸에 총이 있다면 가장 공격력이 높은 총을 획득하고 나머지 총은 내버려둔다.
def lose(loser):
    r, c = x[loser], y[loser]
    if g[loser]:
        guns[r][c].append(g[loser])
        g[loser] = 0

    for i in range(4):
        new_d = (d[loser] + i) % 4  # 가보려는 방향에
        new_r, new_c = r + dr[new_d], c + dc[new_d]
        if in_range(new_r, new_c) and find_player(new_r, new_c) == -1:
            x[loser], y[loser], d[loser] = new_r, new_c, new_d
            check_gun(loser)
            break


# - diff 만큼 점수를 얻는다.
# - row, col로 이동한다.
# - 총을 획득한다.
def win(winner, diff):
    point[winner] += diff
    check_gun(winner)


def solution():
    # 하나의 라운드 진행
    for _ in range(K):
        # 1. 첫 번째 플레이어부터 순차적으로
        for p in range(M):
            new_x, new_y = move(p)  # 플레이어의 방향에 맞춰 이동 '할 예정의' 좌표 반환
            other = find_player(new_x, new_y)  # 다른 사람이 있는지 확인. 없으면 -1

            # [이런실수하지말라고🤬] 여기서 p의 위치 업데이트를 해줘야만 하는 이유. (이걸 또 틀리니)
            # 일단 가려는 곳에 사람이 있든 말든 그 위치로 가야한다. 사람이 있는 경우엔 둘 다 new_x, new_y에서 싸운다.
            # 여기서 업데이트 하지 않으면 진 사람이 움직일 때 다음 위치를 찾는 과정에서
            # 자기랑 겹치고 이긴 사람이랑 겹치고 난리난다.
            x[p], y[p] = new_x, new_y

            # 2-1. 이동할 방향에 플레이어가 '없다'
            if other == -1:
                check_gun(p)  # 총을 확인한다.
            # 2-2.  이동할 방향에 다른 플레이어가 '있다'
            else:
                # 1) 싸운다.
                winner, loser, diff = fight(p, other)  # 상대방이 있으면 싸워서 결과 반환
                # 2) 진 사람
                lose(loser)  # 진 사람 처리
                # 3) 이긴 사람
                win(winner, diff)  # 이긴 사람 처리
    print(*point)

solution()