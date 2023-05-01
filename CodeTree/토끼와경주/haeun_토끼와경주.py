"""
류호석님 영상 : https://www.youtube.com/live/fgDbWXmSZJU?feature=share
이게 왜 골드 1이죠...
왼쪽, 오른쪽, 위, 아래 빠르게 이동하기 위한 테크닉이 필요한데
응 절대 생각 못해 그리고 왕복 한번만 돌아서 또 거기서 틀려

쨌든 이 문제에서 시간초과가 나는 이유는 200 명령 때문이다.
이게 최악의 경우 K(100) * Q(2000) 이며 2*10^5다.
토끼가 최대 2000마리이기 때문에 2000마리를 다 보면 4억번이라 터진다.
그래서 K 턴 돌기 전에 토끼를 heap(PriorityQueue)에 다 넣어놔야 한다.

그리고 선택한 토끼를 빠르게 점프해야한다. 4방향으로 빠르게 움직여봐야한다.
토끼의 거리는 최대 10억이기 때문에 한 칸씩 움직이면 당연히 안된다.
-> 그래서 왕복 한 경우를 제하고, 남은 거리를 구한다. 왕복하고 오면 제자리니깐.
-> 이게 dist %= (N-1) * 2 or (M-1) * 2 가 나오는 이유다.
-> N-1, M-1 을 하는 이유는 이동 가능한 '거리'를 구하는 중이기 때문이다.
근데 이 구해진 거리(dist)를 일일이 뛰면 안된다. N,M의 값이 10만이기 때문이다.
-> 그래서 한 방향으로 끝까지 가보고, 남은 거리를 구해서 반대 방향으로 가본다.
-> 그리고 원래 방향으로 한번 더 가봐야한다.
-> 왜냐하면 왕복 다니는 거리보다 적은 값이라, 각 방향으로 한번씩만 움직이면 되지 않을까? 라고 생각했는데,
-> 기존 토끼의 위치가 끝에 있단 보장이 없기 때문에 원래의 방향으로 한번 더 가야하는 것이다.

예로 토끼의 위치가 (x, 5)이고 M = 7이며, 토끼의 거리는 대충 10만정도로 큰데,
modular 연산을 해보니 남은 거리가 최대값이 되어 11이라고 치자. 왜냐하면 (7-1) * 2 니깐.
그러면 5에서 7까지 오른쪽 방향으로 움직인다. 그럼 토끼의 위치는 (x, 7)이 되고 2만큼 움직였으니 남은 거리는 9다.
이제 왼쪽으로 움직여본다. 토끼의 위치는 (x, 1)이 되고, 6만큼 움직였으니 남은 거리는 3이다.
그래서 오른쪽으로 한번 더 움직여야 하는 것이다. 토끼의 위치는 (x, 4)가 되며 남은 거리는 비로소 0이 된다.
이는 위, 아래, 오른쪽, 왼쪽 모두 적용된다.

어려운 이유는
1. 토끼를 빠르게 이동하는 방법 에 대해 떠올리기 어렵고
2. 그 방법을 구현하는 것도 고려할게 많다.
"""

import heapq

# 전역변수
N, M, P = -1, -1, -1

# 토끼 정보
# key = pid, value = Rabbit
rabbits = dict()

# 전체 점수
total_score = 0


class Rabbit:
    def __init__(self, _pid, _row, _col, _jump, _dist, _score):
        self.pid = _pid  # 고유 번호
        self.row = _row  # 행
        self.col = _col  # 열
        self.jump = _jump  # 점프 횟수
        self.dist = _dist  # 거리
        self.score = _score # 점수

    def __repr__(self):
        return f"🐰 {self.pid}번 토끼 정보 : {self.row} 행, {self.col} 열. 점프 : {self.jump}, 거리 : {self.dist}, 점수 : {self.score}"

    #  1. 현재까지의 총 점프 횟수가 적은 토끼
    #  2. 현재 서있는 행 번호 + 열 번호가 작은 토끼
    #  3. 행 번호가 작은 토끼
    #  4. 열 번호가 작은 토끼
    #  5. 고유번호가 작은 토끼
    def __lt__(self, other):
        if self.jump != other.jump:
            return self.jump < other.jump
        if self.row + self.col != other.row + other.col:
            return self.row + self.col < other.row + other.col
        if self.row != other.row:
            return self.row < other.row
        if self.col != other.col:
            return self.col < other.col
        return self.pid < other.pid


def print_rabbits():
    print("🐰🐰🐰🐰🐰 토끼 전체 출력 🐰🐰🐰🐰🐰")
    for rabbit in rabbits.values():
        print(rabbit)


def print_rabbit(rabbit):
    print("🐰 토끼 출력 🐰")
    print(rabbit)


def init_race(data):
    for i in range(P):
        pid, distance = data[i*2], data[i*2+1]
        # pid, row, col, jump, distance, score
        rabbits[pid] = Rabbit(pid, 1, 1, 0, distance, 0)


# 기존 col의 위치와 이동 거리를 받아와서
# 오른쪽으로 이동한 col을 반환한다. (row 고정)
def right(c, d):
    if M >= c + d:  # 안 넘는다.
        c += d
        d = 0
    else:  # M을 넘어가 버렸다.
        d -= M - c
        c = M

    return c, d


# 기존 col의 위치와 이동 거리를 받아와서
# 왼쪽으로 이동한 col을 반환한다. (row 고정)
def left(c, d):
    # 왼쪽 끝까지 가본다.
    if 1 <= c - d:  # 왼쪽 끝 안 넘는다.
        c -= d
        d = 0
    else:  # 1을 넘어가 버렸다.
        d -= c - 1
        c = 1

    return c, d


# 기존 row의 위치와 이동 거리를 받아와서
# 위쪽으로 이동한 row를 반환한다. (col 고정)
def up(r, d):
    # 위쪽 끝까지 가본다.
    if 1 <= r - d:  # 위쪽 끝 안 넘는다.
        r -= d
        d = 0
    else:  # 1을 넘어가 버렸다.
        d -= r - 1
        r = 1

    return r, d


# 기존 row의 위치와 이동 거리를 받아와서
# 아래쪽으로 이동한 row를 반환한다. (col 고정)
def down(r, d):
    # 아래쪽 끝까지 가본다.
    if N >= r + d:  # 위쪽 끝 안 넘는다.
        r += d
        d = 0
    else:  # 아래쪽 끝을 넘어가 버렸다.
        d -= N - r
        r = N

    return r, d


def get_goal(row, col, dist):
    pos = []

    # 이건 진짜 복습 어떻게 해야할지도 모르겠다
    # 오른쪽
    r_dist = dist % ((M - 1) * 2)
    r_col, r_dist = right(col, r_dist)
    r_col, r_dist = left(r_col, r_dist)
    r_col, r_dist = right(r_col, r_dist)
    pos.append((row + r_col, row, r_col))

    # 왼쪽
    l_dist = dist % ((M - 1) * 2)
    l_col, l_dist = left(col, l_dist)
    l_col, l_dist = right(l_col, l_dist)
    l_col, l_dist = left(l_col, l_dist)
    pos.append((row + l_col, row, l_col))

    # 위쪽
    u_dist = dist % ((N - 1) * 2)
    u_row, u_dist = up(row, u_dist)
    u_row, u_dist = down(u_row, u_dist)
    u_row, u_dist = up(u_row, u_dist)
    pos.append((u_row + col, u_row, col))

    # 아래쪽
    d_dist = dist % ((N - 1) * 2)
    d_row, d_dist = down(row, d_dist)
    d_row, d_dist = up(d_row, d_dist)
    d_row, d_dist = down(d_row, d_dist)
    pos.append((d_row + col, d_row, col))

    # print(f" {b_rabbit.pid}번 토끼 위치 : {row, col}, 거리 : {dist}")
    # print(pos)
    # 3. 가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼를 이동시킵니다.
    pos.sort(key=lambda x: [-x[0], -x[1], -x[2]])
    _, best_row, best_col = pos[0]
    return best_row, best_col


def compare(me, you):
    #  1. 현재 서있는 행 번호 + 열 번호가 큰 토끼
    if me.row + me.col != you.row + you.col:
        return me.row + me.col < you.row + you.col
    #  2. 행 번호가 큰 토끼
    if me.row != you.row:
        return me.row < you.row
    #  3. 열 번호가 큰 토끼
    if me.col != you.col:
        return me.col < you.col
    #  4. 고유번호가 큰 토끼
    return me.pid < you.pid


# 가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 K번 반복합니다.
def race(K, S):
    global total_score
    # 한번이라도 뽑혔던 토끼가 필요하다.
    picked = set()

    # 우선순위
    priority = []
    for rabbit in rabbits.values():
        heapq.heappush(priority, rabbit)

    for _ in range(K):
        # 1. 이번에 점프할 토끼 선정하기 O(logP)
        # 첫 번째 우선순위가 높은 토끼가 한마리 뿐이라면 바로 결정되는 것이고, 동률이라면 두 번째 우선순위를 보고...
        # 이러한 규칙에 의해 가장 우선순위가 높은 토끼가 결정됩니다.
        # 우선순위가 가장 높은 토끼 결정
        b_rabbit = heapq.heappop(priority)

        # 2. 이동할 위치 선정하기
        # 이 토끼를 i번 토끼라 했을 때 상하좌우 네 방향으로 각각 di만큼 이동했을 때의 위치를 구합니다.
        # 이렇게 구해진 4개의 위치 중 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순으로 우선순위로 둔다.
        # 1 <= di <= 10^9 한 칸씩 움직이면 안된다....

        b_rabbit.row, b_rabbit.col = get_goal(b_rabbit.row, b_rabbit.col, b_rabbit.dist)
        b_rabbit.jump += 1
        picked.add(b_rabbit.pid)

        heapq.heappush(priority, b_rabbit)

        # 4. 점수 업데이트
        # 이 칸의 위치를 (ri,ci)라 했을 때 i번 토끼를 제외한 나머지 P−1마리의 토끼들은 전부 ri+ci만큼의 점수를 동시에 얻게 됩니다.
        b_rabbit.score -= (b_rabbit.row + b_rabbit.col)
        total_score += (b_rabbit.row + b_rabbit.col)

        # 이렇게 K번의 턴 동안 가장 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 반복하게 되며,
        # 이 과정에서 동일한 토끼가 여러번 선택되는 것 역시 가능합니다.

    # 5. K번의 턴이 모두 진행된 직후에는 아래의 우선순위대로 둡니다.
    # 맨 앞에껄 꺼냈는데 생각해보니 걔가 점프를 안했을 수도 있어서...
    final_rabbit = Rabbit(0, 0, 0, 0, 0, 0)
    while priority:
        other = heapq.heappop(priority)
        #  (단, 이 경우에는 K번의 턴 동안 한번이라도 뽑혔던 적이 있던 토끼 중 가장 우선순위가 높은 토끼를 골라야만 함에 꼭 유의합니다.)
        if other.pid in picked:
            if compare(final_rabbit, other):
                final_rabbit = other

    #  가장 우선순위가 높은 토끼를 골라 점수 S를 더해주게 됩니다.
    final_rabbit.score += S


def change_dist(r_pid, length):
    rabbits[r_pid].dist *= length


def get_best():
    max_score = 0
    for pid in rabbits:
        max_score = max(max_score, rabbits[pid].score)

    print(max_score  + total_score)


def solution():
    global N, M, P
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        order = query[0]
        if order == 100:
            N, M, P = query[1], query[2], query[3]
            init_race(query[4:])
        elif order == 200:
            race(query[1], query[2])
        elif order == 300:
            change_dist(query[1], query[2])
        elif order == 400:
            get_best()


solution()