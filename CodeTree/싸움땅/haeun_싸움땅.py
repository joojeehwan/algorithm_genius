"""
정답 : k 라운드 동안 게임을 진행하며, 각 플레이어들이 획득한 포인트를 출력
"""

import sys
sys.stdin = open("input.txt", "r")



class Player:
    def __init__(self, row, col, direct, skill, gun):
        self.r = row
        self.c = col
        self.d = direct
        self.s = skill
        self.g = gun

    def __repr__(self):
       return f"플레이어 => 위치 : {self.r, self.c} || 방향 : {self.d} || 능력치 : {self.s} || 총 : {self.g}"


# 입력 처리
N, M, K = map(int, input().split())  # 격자 크기, 플레이어 수, 라운드 횟수

players = []
guns = [[[] for _ in range(N)] for _ in range(N)]

# 0보다 큰 공격력을 가진 경우, 해당 위치에 총으로 저장
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(N):
        if line[c]:
            guns[r][c].append(line[c])

# 플레이어 정보 받기
for idx in range(M):
    x, y, d, s = map(int, input().split())
    players.append(Player(x - 1, y - 1, d, s, 0))  # 5번째는 총이다.

# 전역 변수
dr = [-1, 0, 1, 0]  #(상, 우, 하, 좌)
dc = [0, 1, 0, -1]
answer = [0] * M


def print_guns():
    print("🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫")
    for r in range(N):
            print(*guns[r])
    print("🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫")


def print_players():
    print("#################### All 플레이어 ######################")
    for i in range(M):
        p = players[i]
        print(f"{i}번째 플레이어 => 위치 : {p.r, p.c} || 방향 : {p.d} || 능력치 : {p.s} || 총 : {p.g}")
    print()


def print_two_player(a, b):
    print(f"%%%%%%%%%%%%%% {a}와 {b}의 진검 승부 %%%%%%%%%%%%%%%%%%")
    pa = players[a]
    pb = players[b]
    print(f"{a}번째 플레이어 => 위치 : {pa.r, pa.c} || 방향 : {pa.d} || 능력치 : {pa.s} || 총 : {pa.g}")
    print(f"{b}번째 플레이어 => 위치 : {pb.r, pb.c} || 방향 : {pb.d} || 능력치 : {pb.s} || 총 : {pb.g}")
    print()


def in_range(row, col):
    return 0 <= row < N and 0 <= col < N


def is_there(my_idx, my_row, my_col):
    for other in range(M):
        if other == my_idx:
            continue
        if players[other].r == my_row and players[other].c == my_col:
            return other
    return -1


def check_gun(player):
    # 플레이어가 총을 가지고 있다면 비교하여 가장 공격력이 쎈 총을 획득하고 나머지는 내려둠
    if player.g:
        guns[player.r][player.c].append(player.g)
    if guns[player.r][player.c]:
        guns[player.r][player.c].sort(reverse=True)
        player.g = guns[player.r][player.c][0]
        guns[player.r][player.c].pop(0)


def fight(i, j):
    # 초기 능력지 + 총의 공격력 을 비교하여 더 큰 사람이 승리.
    me_power = players[i].s + players[i].g
    you_power = players[j].s + players[j].g
    diff = abs(me_power - you_power)
    if me_power > you_power:
        return i, j, diff
    elif me_power < you_power:
        return j, i, diff
    else:
        # 동일한 경우 초기 능력치가 높은 사람이 승리.
        if players[i].s > players[j].s:
            return i, j, diff
        else:
            return j, i, diff


def lost(l):
    loser = players[l]
    # 진 사람은 총을 내려놓고, 원래 방향으로 한칸 이동하는데,
    if loser.g:
        guns[loser.r][loser.c].append(loser.g)
        loser.g = 0

    for i in range(4):
        n_dir = (loser.d + i) % 4
        n_row, n_col = loser.r + dr[n_dir], loser.c + dc[n_dir]
        # 이미 플레이어가 있거나 격자 밖인 경우 오른쪽으로 90도 회전하며 빈칸이 있으면 이동.
        if not in_range(n_row, n_col) or (is_there(l, n_row, n_col) != -1):
            continue
        else:
            loser.r, loser.c, loser.d = n_row, n_col, n_dir
            # 해당 칸에 총이 있다면 가장 공격력이 쎈 총을 획득하고 나머지는 내려둠.
            check_gun(loser)
            break


def solution():
    for m in range(M):
        me = players[m]
        # 첫 번째 플레이어부터 순차적으로 본인의 방향으로 한 칸 이동
        if not in_range(me.r + dr[me.d], me.c + dc[me.d]):
            # 격자를 벗어나는 경우 정반대 방향으로 한 칸 이동
            me.d = (me.d + 2) % 4

        me.r += dr[me.d]
        me.c += dc[me.d]

        other = is_there(m, me.r, me.c)  # 가려는 곳에 누군가 있는가? (있다면 인덱스 반환)

        if other != -1:
            # 이동한 곳에 플레이어가 있다면 싸운다.
            win, lose, diff = fight(m, other)
            # 이긴 사람은 둘의 (초기 능력치 + 총의 공격력) 차이만큼 포인트 획득.
            answer[win] += diff

            lost(lose)
            # 이긴 사람은 승리한 칸에 있는 총과 원래 총 중 가장 공격력이 쎈 총을 획득하고, 나머지는 내려둠.
            check_gun(players[win])
        else:
            # 이동한 곳에 플레이어가 없다면 총 확인
            check_gun(me)


for _ in range(K):
    solution()
    # print_guns()
    print_players()
    print(f"{_}번째 턴")
    print(*answer)

print(*answer)
