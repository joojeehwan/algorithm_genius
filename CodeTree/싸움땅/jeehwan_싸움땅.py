'''

n * n 격자

초기에는 무기들이 없는 빈 격자에 플레이어들이 위치 함. -> 각 플레이어는 초기 능력치를 가짐.(각자 다 다름)


빨간색 배경의 무기 숫자 -> 초기 능력치

빨간색 배경의 플레이어 숫자 -> 무기 공격력

노란색 벼경의 숫자 -> 플레이어의 숫자


라운드 진행과정


1. 첫 번쨰 플레이어 부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동. 만약, 격자를 벗어나는 경우 정반대 방향으로 방향을 바꾸어서 1만큼 이동


2.  1) 만약 이동한 방향에 플레이어가 없다면,
        => 총이 있는지 확인 총이 있는 경우 플레이어는 총을 획득
           이미 총이 있는 경우?! 놓여있는 총들과 가지고 있는 총 중에서 가장 강한 총을 획득, 나머지는 다시 격자에


    2) - 1 만약 이동한 방향에 플레이어가 있다면?
        => 두 플레이어는 싸운다. (초기 능력치 + 가지고 있는 총의 공격력), 더 큰 플레이어가 이긴다.
        => 만약, 이 수치가 같은 경우 초기 능력치가 큰 플레이어가 이김
        => 이긴 플레이어는 진 플레이어의 (초기 능력치 + 가지고 있는 총의 공격력) 합의 차이 만큼 포인트 획득


       - 2 진 플레이어는 본인이 가진 총을 내려다 놓고, 해당 플레이어(진 플레이어)가 가지고 있던 원래 방향으로 한 칸 이동.
           만약 이동하려는 칸에 다른 플레이어?! 혹은 격자 범위 밖인 경우  오른쪽으로 90도 씩 회전하면 빈칸이 보이는 순간 이동
           만약 해당 칸에 총이 있다면?! 가장 공격력이 높은 것을 취득, 나머지는 내려놓기

       - 3 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 있던 총들 중에서 가장 공력이 높은 총을 획득하고, 나머지는 총을 다시 격자에


위의 과정을 1번부 n번까지 "순서대로" 한 번씩 진행


k라운드 동안 게임을 진행하면서, 각 플레이어들이 획득한 포인트를 출력


'''


#정답 풀이

EMPTY = (-1, -1, -1, -1, -1, -1)

# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))

# 각 칸마다 놓여있는 총 목록을 관리합니다.
gun = [
    [[] for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        # 총이 놓여 있는 칸입니다.
        if nums[j] != 0:
            gun[i][j].append(nums[j])

# 각 칸마다 플레이어 정보를 관리합니다.
# 순서대로 (num, x, y, d, s, a) 정보를 관리합니다.
# (x, y)위치에서 방향 d를 보고 있으며
# 초기 능력치가 s인 num번 플레이어가
# 공격력이 a인 총을 들고 있음을 뜻합니다.
# 총이 없으면 a는 0입니다.

#그냥 tuple로 넣고 싶으면, 큰 [] 하나 만들어 놓고, 그냥 넣으면 된다...!
players = []
for i in range(m):
    x, y, d, s = tuple(map(int, input().split()))
    players.append((i, x - 1, y - 1, d, s, 0))

print(players)
# 입력으로 주어지는
# 방향 순서대로 
# dx, dy를 정의합니다.
# ↑, →, ↓, ←
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 플레이어들의 포인트 정보를 기록합니다.
# 굳이 하나로 모을 필요가 없다. 그냥 뺴면 된다잉!
points = [0] * m


# (x, y)가 격자를 벗어나는지 확인합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 현재 (x, y)위치에서 방향 d를 보고 있을 때
# 그 다음 위치와 방향을 찾아줍니다.
def get_next(x, y, d):
    nx, ny = x + dxs[d], y + dys[d]
    # 격자를 벗어나면
    # 방향을 뒤집어
    # 반대 방향으로 한 칸 이동합니다.
    if not in_range(nx, ny):
        # 반대 방향 : 0 <. 2 / 1 <. 3
        d = (d + 2) if d < 2 else (d - 2)
        nx, ny = x + dxs[d], y + dys[d]

    return (nx, ny, d)


# 해당 칸에 있는 Player를 찾아줍니다.
# 없다면 EMPTY를 반환합니다.
def find_player(pos):
    for i in range(m):
        _, x, y, _, _, _ = players[i]
        if pos == (x, y):
            return players[i]

    return EMPTY


# Player p의 정보를 갱신해줍니다.
def update(p):
    num, _, _, _, _, _ = p

    # Player의 위치를 찾아
    # 값을 갱신해줍니다.
    for i in range(m):
        num_i, _, _, _, _, _ = players[i]

        if num_i == num:
            players[i] = p
            break


# 플레이어 p를 pos 위치로 이동시켜줍니다.
def move(p, pos):
    num, x, y, d, s, a = p
    nx, ny = pos

    # 가장 좋은 총으로 갱신해줍니다.
    gun[nx][ny].append(a)
    '''
    여기가 가장 큰 차이점을 갖는다. 
    나 같은 경우는 append하고 clear 해서 그랬는데, 
    굳이 그럴필요 없이, 어차피 안에 배열이니깐 가장 큰 값을 reverse=True로 가져오면 된다.
    그리고 할당을 하고, pop을 하면?! 아주 깔끔하게 풀 수 있다.
    
    '''
    gun[nx][ny].sort(reverse=True)
    a = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    p = (num, nx, ny, d, s, a)
    update(p)


# 진 사람의 움직임을 진행합니다.
# 결투에서 패배한 위치는 pos입니다.
def loser_move(p):
    num, x, y, d, s, a = p

    # 먼저 현재 위치에 총을 내려놓게 됩니다.
    gun[x][y].append(a)

    # 빈 공간을 찾아 이동하게 됩니다.
    # 현재 방향에서 시작하여
    # 90'씩 시계방향으로
    # 회전하다가 
    # 비어있는 최초의 곳으로 이동합니다.
    for i in range(4):
        ndir = (d + i) % 4
        nx, ny = x + dxs[ndir], y + dys[ndir]
        if in_range(nx, ny) and find_player((nx, ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0)
            move(p, (nx, ny))
            break


# p2과 p2가 pos에서 만나 결투를 진행합니다.
def duel(p1, p2, pos):
    num1, _, _, d1, s1, a1 = p1
    num2, _, _, d2, s2, a2 = p2

    # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로 우선순위를 매겨 비교합니다.

    # p1이 이긴 경우
    if (s1 + a1, s1) > (s2 + a2, s2):
        # p1은 포인트를 얻게 됩니다.
        points[num1] += (s1 + a1) - (s2 + a2)
        # p2는 진 사람의 움직임을 진행합니다.
        loser_move(p2)
        # 이후 p1은 이긴 사람의 움직임을 진행합니다.
        move(p1, pos)
    # p2가 이긴 경우
    else:
        # p2는 포인트를 얻게 됩니다.
        points[num2] += (s2 + a2) - (s1 + a1)
        # p1은 진 사람의 움직임을 진행합니다.
        loser_move(p1)
        # 이후 p2는 이긴 사람의 움직임을 진행합니다.
        move(p2, pos)


# 1라운드를 진행합니다.
def simulate():
    # 첫 번째 플레이어부터 순서대로 진행합니다.
    for i in range(m):
        num, x, y, d, s, a = players[i]

        # Step 1-1. 현재 플레이어가 움직일 그 다음 위치와 방향을 구합니다.
        nx, ny, ndir = get_next(x, y, d)

        # 해당 위치에 있는 전 플레이어 정보를 얻어옵니다.
        next_player = find_player((nx, ny))

        # 현재 플레이어의 위치와 방향을 보정해줍니다.
        curr_player = (num, nx, ny, ndir, s, a)
        update(curr_player)

        # Step 2. 해당 위치로 이동해봅니다.
        # Step 2-1. 해당 위치에 플레이어가 없다면 그대로 움직입니다.
        if next_player == EMPTY:
            move(curr_player, (nx, ny))
        # Step 2-2. 해당 위치에 플레이어가 있다면 결투를 진행합니다.
        else:
            duel(curr_player, next_player, (nx, ny))


# k번에 걸쳐 시뮬레이션을 진행합니다.
for _ in range(k):
    simulate()

# 각 플레이어가 획득한 포인트를 출력합니다.
for point in points:
    print(point, end=" ")


'''
풀이 1
'''


def change_weapon(idx, y, x):
    # idx 검투사가 (x,y)에서 무기 선택하는 행위
    if field[y][x] and warriors[idx][4] > field[y][x][0]:
        # 현재 무기보다 해당 위치에 있는 가장 쎈 무기가 더 좋은 경우(음수)
        # 지금 무기 집어넣고 가장 좋은 무기 선택
        warriors[idx][4] = heapq.heappushpop(field[y][x], warriors[idx][4])

    war_field[y][x] = idx  # 해당 위치에 싸움꾼 정보 업데이트
    warriors[idx][0], warriors[idx][1] = y, x
    return


def throw_weapon(idx, y, x):
    # 현재 들고 있는 무기 버리기
    heapq.heappush(field[y][x], warriors[idx][4])
    warriors[idx][4] = 0  # 무기 버린 상태
    return


def fight(cur_idx, foe_idx):
    # 두 싸움꾼 번호가 주어졌을 때, 상대방의 승리 여부 체크
    cur_stat, cur_weapon = warriors[cur_idx][3], warriors[cur_idx][4]
    foe_stat, foe_weapon = warriors[foe_idx][3], warriors[foe_idx][4]

    if cur_stat - cur_weapon < foe_stat - foe_weapon:
        # 상대방의 스탯+무기 공격력이 더 큰 경우
        score[foe_idx] += (foe_stat - foe_weapon) - (cur_stat - cur_weapon)
        return True
    elif cur_stat - cur_weapon == foe_stat - foe_weapon and cur_stat < foe_stat:
        # 스탯+무기 공격력은 같은데, 상대방 기초 스탯이 더 높은 경우
        # 점수 업데이트는 없음
        return True
    # 이동한 싸움꾼이 이긴 경우
    score[cur_idx] += (cur_stat - cur_weapon) - (foe_stat - foe_weapon)
    return False


def loser_move(idx, y, x):
    throw_weapon(idx, y, x)  # 무기 현재 위치에 버림
    l_dir = warriors[idx][2]  # 패자 초기 방향
    for _ in range(4):
        n_y, n_x = y + dir[l_dir][0], x + dir[l_dir][1]
        if 0 <= n_y < n and 0 <= n_x < n and not war_field[n_y][n_x]:
            # 이동하고자 하는 곳이 필드 내부면서, 그 위치에 다른 싸움꾼이 없다면
            change_weapon(idx, n_y, n_x)  # 이동해서 무기 교체
            # 패자 정보 업데이트
            war_field[n_y][n_x] = idx
            warriors[idx][1], warriors[idx][0] = n_x, n_y
            warriors[idx][2] = l_dir
            return
        l_dir = (l_dir + 1) % 4  # 이동 못하면 방향 90도 전환
    return


def war_round():
    for idx in range(1, m + 1):
        cur_man = warriors[idx]  # idx번 검투사 움직일 차례
        cur_x, cur_y, cur_dir = cur_man[1], cur_man[0], cur_man[2]

        next_y, next_x = cur_y + dir[cur_dir][0], cur_x + dir[cur_dir][1]  # 움직인 위치
        if not (0 <= next_y < n and 0 <= next_x < n):  # 격자 바깥으로 나간다면
            cur_dir = (cur_dir + 2) % 4  # 방향 180도 전환
            warriors[idx][2] = cur_dir
            next_y, next_x = cur_y + dir[cur_dir][0], cur_x + dir[cur_dir][1]  # 움직인 위치

        # cur_man[0], cur_man[1], cur_man[2] = next_y, next_x, cur_dir # 최종 이동 위치 및 방향 업데이트
        war_field[cur_y][cur_x] = 0  # 이동했으니 원래 위치에서 싸움꾼 정보 제거

        if war_field[next_y][next_x]:  # 움직인 위치에 다른 싸움꾼이 있다면
            foe_idx = war_field[next_y][next_x]  # 해당 위치에 있던 싸움꾼 번호

            foe_win = fight(idx, foe_idx)  # 누가 이겼는지 체크

            if foe_win:  # 상대방 승리
                loser_move(idx, next_y, next_x)
                change_weapon(foe_idx, next_y, next_x)
            else:  # idx 싸움꾼 승리
                loser_move(foe_idx, next_y, next_x)
                change_weapon(idx, next_y, next_x)

        else:  # 움직인 위치에 상대방이 없다면
            change_weapon(idx, next_y, next_x)


if __name__ == "__main__":
    import heapq

    n, m, k = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]  # 무기 위치 저장되는 필드
    warriors = [0] + [list(map(int, input().split())) + [0] for _ in range(m)]  # 제공되는 싸움꾼 정보 + 무기 정보
    # 각 싸움꾼의 x, y, 방향, 능력치, 무기

    for y in range(n):
        for x in range(n):
            # 무기 위치 힙 사용하기 위해 지도 각 위치 리스트 처리
            # max heap 위해 무기 공격력 음수 처리
            if field[y][x]:
                field[y][x] = [-field[y][x]]
            else:
                field[y][x] = []

    war_field = [[0] * n for _ in range(n)]  # 싸움꾼의 위치를 저장하기 위한 필드
    for idx, man in enumerate(warriors):
        if idx == 0: continue
        man[0] -= 1
        man[1] -= 1
        x, y = man[1], man[0]  # idx번 싸움꾼의 좌표
        war_field[y][x] = idx  # 해당 위치에 몇 번 싸움꾼이 있는지 저장

    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상우하좌
    score = [0] * (m + 1)  # 점수 저장용

    for _ in range(k):
        war_round()

    print(*score[1:])



'''

풀이 2

'''

def move_guns(player_num):
    # 플레이어가 총이 없는 경우
    if player[player_num][4] == 0:
        player[player_num][4] = max(guns[nx][ny])
        del guns[nx][ny][guns[nx][ny].index(max(guns[nx][ny]))]
    # 플레이어가 총이 있는 경우
    else:
        #플레이어의 총보다 바닥의 총이 공격력이 쌘 경우
        if max(guns[nx][ny]) > player[player_num][4]:
            tmp = player[player_num][4]
            player[player_num][4] = max(guns[nx][ny])
            del guns[nx][ny][guns[nx][ny].index(max(guns[nx][ny]))]
            guns[nx][ny].append(tmp)  # 기존 총을 바닥에 버림
    graph[nx][ny] = 0  # 이동한 자리 사람 마킹

def player_fight():
    player_idx = []
    for i in range(len(player_posit)):
        if player_posit[i] == (nx,ny):
            player_idx.append(i)
    #점수 계산
    score1 = [player[player_idx[0]][3] + player[player_idx[0]][4], player[player_idx[0]][3], player_idx[0]]
    score2 = [player[player_idx[1]][3] + player[player_idx[1]][4], player[player_idx[1]][3], player_idx[1]]
    tmp = []
    tmp.append(score1)
    tmp.append(score2)
    tmp.sort(reverse=True)
    score[tmp[0][2]-1] += tmp[0][0] - tmp[1][0]


    #진 플레이어
    loser = tmp[1][2]
    lose_gun = player[loser][4]
    #가진 총이 있다면 내려놓음
    if player[loser][4] != 0:
        guns[nx][ny].append(lose_gun)
        player[loser][4] = 0


    next_d = player[loser][2]
    #방향 찾기
    for _ in range(4):
        next_x = nx + dx[next_d]
        next_y = ny + dy[next_d]
        if not(0 <= next_x < n and 0 <= next_y < n) or graph[next_x][next_y] == 0:
            next_d = (next_d + 1) % 4
        else:
            break
    #좌표 없뎃
    player_posit[loser] = (next_x, next_y)
    player[loser][0], player[loser][1], player[loser][2] = next_x, next_y, next_d


    #가장 공격력이 쌘 총을 주음
    if graph[next_x][next_y] != -1:
        player[loser][4] = max(guns[next_x][next_y])
        #공격력 쌘 총을 바닥에서 없앰
        del guns[next_x][next_y][guns[next_x][next_y].index(max(guns[next_x][next_y]))]

    graph[next_x][next_y] = 0  # 그래프 업뎃

    #이긴 플레이어
    winner = tmp[0][2]
    if guns[nx][ny]:
        if max(guns[nx][ny]) > player[winner][4]:
            tmp_gun = player[winner][4]
            player[winner][4] = max(guns[nx][ny])
            del guns[nx][ny][guns[nx][ny].index(max(guns[nx][ny]))]
            guns[nx][ny].append(tmp_gun)  # 기존 총을 바닥에 버림

#n:격자 크기 m:플레이어의 수, k:라운드수
n ,m, k = map(int, input().split())
#총의 정보
graph = [list(map(int, input().split())) for _ in range(n)] # 0은 인간, -1은 빈칸, 나머지는 총
guns = [[[] for _ in range(n)] for _ in range(n)]

#총의 상태 그래프
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            guns[i][j].append(graph[i][j])

player = {}
score = [0] * m

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

player_posit = [[]]
#[x, y, 방향, 기본스텟, 총보유]
for i in range(1, m+1):
    player[i] = list(map(int, input().split())) + [0]
    player[i][0] -= 1
    player[i][1] -= 1
    player_posit.append((player[i][0], player[i][1]))

#사람이 없는 빈칸을 -1로 다시 변환
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and (i,j) not in player_posit:
            graph[i][j] = -1


for num in range(k):
    #플레이어의 이동
    for i in range(1, m+1):
        x, y, d  = player[i][0], player[i][1], player[i][2]
        nx = x + dx[d]
        ny = y + dy[d]
        #2-1 이동 칸에 총이 있는 경우 2-2플레이어가 있는 경우 1) 이긴 플레이어 2) 진 플레이어
        if not (0 <= nx < n and 0 <= ny < n):
            nx = x - dx[d]
            ny = y - dy[d]
            d = (d + 2) % 4

        #이동 칸에 총이 있는 경우
        if graph[nx][ny] > 0:
            player_posit[i] = (nx, ny)
            player[i][0], player[i][1], player[i][2] = nx, ny, d
            if not guns[x][y]:
                graph[x][y] = -1  # 기존 자리 빈칸
            else:
                graph[x][y] = max(guns[x][y])
            move_guns(i)

        #이동한 칸에 플레이어가 잇는 경우
        elif graph[nx][ny] == 0:
            if not guns[x][y]:
                graph[x][y] = -1  # 기존 자리 빈칸
            else:
                graph[x][y] = max(guns[x][y])
            player_posit[i] = (nx, ny)
            player[i][0], player[i][1], player[i][2] = nx, ny, d

            player_fight()

        #이동 칸이 빈칸인 경우
        else:
            player_posit[i] = (nx, ny)
            player[i][0], player[i][1], player[i][2] = nx, ny, d
            graph[nx][ny] = 0
            if not guns[x][y]:
                graph[x][y] = -1  # 기존 자리 빈칸
            else:
                graph[x][y] = max(guns[x][y])

print(' '.join(map(str,score)))