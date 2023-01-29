n, m, k = map(int, input().split())
MAP = list(list(map(int, input().split())) for _ in range(n))
pos = [[0] * n for _ in range(n)]
guns = dict()
players = []
score = [0] * (m+1)
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


class Player:
    def __init__(self, r, c, d, s, w):
        self.row = r
        self.col = c
        self.dir = d
        self.skill = s
        self.weapon = w

    def __repr__(self):
        return f"위치 : {self.row} , {self.col} | 방향 : {self.dir} | 능력 : {self.skill} | 무기 : {self.weapon}"


def print_players():
    for i in range(m):
        print(i+1, "번 => ", players[i+1])


def lost(l, r, c):
    # 일단 총 내려놔
    loser = players[l]
    if loser.weapon:
        guns[(r, c)] = guns.get((r, c), [])
        guns[(r, c)].append(loser.weapon)
        loser.weapon = 0

    for i in range(4):
        loser.dir = (loser.dir + i) % 4
        nr, nc = r + dr[loser.dir], c + dc[loser.dir]

        if 0 > nr or n <= nr or 0 > nc or n <= nc or pos[nr][nc]:
            # 응 못가 회전해
            continue
        else:
            loser.row, loser.col = nr, nc
            pos[nr][nc] = l

            if guns.get((nr, nc)):
                change_gun(loser, nr, nc)
            break


def won(w, r, c):
    winner = players[w]
    winner.row, winner.col = r, c
    pos[r][c] = w
    if guns.get((r, c)):
        change_gun(winner, r, c)


def fight(m, y):
    me, you = players[m], players[y]
    me_f, you_f = me.skill + me.weapon, you.skill + you.weapon

    if me_f == you_f:
        if me.skill > you.skill:
            win, lose = m, y
        else:
            win, lose = y, m
    elif me_f > you_f:
        win, lose = m, y
    else:
        win, lose = y, m

    dif = (players[win].skill + players[win].weapon) - (players[lose].skill + players[lose].weapon)
    score[win] += dif
    return win, lose


def change_gun(player, r, c):
    gun = guns.get((r, c))
    gun.sort()
    strong = gun.pop()
    if player.weapon < strong:
        if player.weapon > 0:
            gun.append(player.weapon)
        if not gun:
            guns.pop((r, c))
        player.weapon = strong
    else:
        gun.append(strong)


def move(me, nr, nc):
    # 다른 사람이 있다면 싸운다!
    if pos[nr][nc]:
        winner, loser = fight(me, pos[nr][nc])
        lost(loser, nr, nc)
        won(winner, nr, nc)
    else:
        pos[nr][nc] = me
        player = players[me]
        player.row, player.col = nr, nc

        if guns.get((nr, nc)):
            change_gun(player, nr, nc)


def simulate():
    for _ in range(k):
        for p in range(1, m + 1):
            player = players[p]
            nr, nc = player.row + dr[player.dir], player.col + dc[player.dir]
            if 0 > nr or n <= nr or 0 > nc or n <= nc:
                # 반대방향으로 가!
                player.dir = (player.dir + 2) % 4
                nr, nc = player.row + dr[player.dir], player.col + dc[player.dir]
            pos[player.row][player.col] = 0
            move(p, nr, nc)



def init():
    # 총 정보 dictionary로 저장
    for r in range(n):
        for c in range(n):
            if MAP[r][c]:
                guns[(r, c)] = [MAP[r][c]]

    # 플레이어 정보 저장
    players.append(Player(-1, -1, -1, -1, -1))
    for i in range(m):
        r, c, d, s = map(int, input().split())
        players.append(Player(r-1, c-1, d, s, 0))
        pos[r-1][c-1] = i+1

    simulate()


init()


print(" ".join(map(str, score[1:])))