
#1 bfs 풀이

from collections import deque

# 우 상 좌 하
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def find_group(x, y):
    q = deque([(x, y)])
    locations = [(board[x][y], x, y)]
    groups[x][y] = group_num

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] and not groups[nx][ny]:
                    if board[x][y] == 1 and board[nx][ny] == 3: continue
                    groups[nx][ny] = group_num
                    q.append((nx, ny))
                    if board[nx][ny] != 4:
                        locations.append((board[nx][ny], nx, ny))
    return locations

def move_team(num):
    head, x, y = group_info[num][0]
    tmp = []
    flag = False
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 4:
                board[nx][ny] = head #1이 담기겟네?!
                tmp.append((head, nx, ny))
                flag = True
                break
    for i in range(len(group_info[num])):

        if i == 0 and flag:
            continue

        now, x, y = group_info[num][i]
        before, bx, by = group_info[num][i - 1]
        tmp.append((now, bx, by))
        board[bx][by] = now
        board[x][y] = 4

    head, hx, hy = tmp[0]
    tail, tx, ty = tmp[-1]
    board[hx][hy] = 1
    board[tx][ty] = 3

    group_info[num] = tmp

def find_arrow(now_time):
    global ans
    a, b = (now_time // n) % 4, now_time % n
    if a == 0:
        for j in range(n):
            if board[b][j] and board[b][j] != 4:
                group_number = groups[b][j]
                for idx, (p, x, y) in enumerate(group_info[group_number]):
                    if (x, y) == (b, j):
                        ans += (idx + 1) ** 2
                        break
                group_info[group_number].reverse()
                head, hx, hy = group_info[group_number][0]
                tail, tx, ty = group_info[group_number][-1]
                board[hx][hy], board[tx][ty] = board[tx][ty], board[hx][hy]
                break
    elif a == 1:
        for i in range(n - 1, -1, -1):
            if board[i][b] and board[i][b] != 4:
                group_number = groups[i][b]
                for idx, (p, x, y) in enumerate(group_info[group_number]):
                    if (x, y) == (i, b):
                        ans += (idx + 1) ** 2
                        break
                group_info[group_number].reverse()
                head, hx, hy = group_info[group_number][0]
                tail, tx, ty = group_info[group_number][-1]
                board[hx][hy], board[tx][ty] = board[tx][ty], board[hx][hy]
                break
    elif a == 2:
        for j in range(n - 1, -1, -1):
            if board[n - 1 - b][j] and board[n - 1 - b][j] != 4:
                group_number = groups[n - 1 - b][j]
                for idx, (p, x, y) in enumerate(group_info[group_number]):
                    if (x, y) == (n - 1 - b, j):
                        ans += (idx + 1) ** 2
                        break
                group_info[group_number].reverse()
                head, hx, hy = group_info[group_number][0]
                tail, tx, ty = group_info[group_number][-1]
                board[hx][hy], board[tx][ty] = board[tx][ty], board[hx][hy]
                break
    elif a == 3:
        for i in range(n):
            if board[i][n - 1 - b] and board[i][n - 1 - b] != 4:
                group_number = groups[i][n - 1 - b]
                for idx, (p, x, y) in enumerate(group_info[group_number]):
                    if (x, y) == (i, n - 1 - b):
                        ans += (idx + 1) ** 2
                        break
                group_info[group_number].reverse()
                head, hx, hy = group_info[group_number][0]
                tail, tx, ty = group_info[group_number][-1]
                board[hx][hy], board[tx][ty] = board[tx][ty], board[hx][hy]
                break

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    time, ans = 0, 0

    groups = [[0] * n for _ in range(n)]
    group_num = 1
    group_info = [[] for _ in range(m + 1)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                group_info[group_num] = find_group(i, j)
                group_num += 1

    while time < k:
        # 각 팀 한칸 이동
        for i in range(1, group_num):
            move_team(i)
        # 턴 수에 따른 화살표 계산 + 점수 계산 + 위치 변경
        find_arrow(time)
        # 다음 라운드
        time += 1
    print(ans)



#2 bfs풀이

# 12:35
import copy

# nxn 격자에서 꼬리잡기
# 3명 이상이 한팀이 됨
# 맨앞은 머리사람, 맨뒤 꼬리사람
# 각 팀은 게임에서 주어진 동선에 따라 이동
# 각 팀의 동선은 끝이 이어져있고, 팀끼리의 동선 겹치지 않음



n, m, k = map(int, input().split())
temp_route_map = []
route_map = [[0]*n for _ in range(n)]
pp_group = [0]*(m+1)

head = [[]] #팀 번호는 1붙터 시작
tail = []
for i in range(n):
    # 0 빈칸/ 1 머리사람 / 2 걍 사람  / 3 꼬리 사람 / 4 이동선
    temp = list(map(int, input().split()))
    temp_route_map.append(temp)
    for j in range(n):
        if temp[j] == 1:
            head.append([i, j])
        elif temp[j] == 3:
            tail.append([i, j])
#방향 벡터 오른 위 왼 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

##### route map 만들기######
from collections import deque
def make_group(hx, hy, tn):
    my_team = [[hx, hy]]
    visited[hx][hy] = True
    pp_group[tn] += 1
    q = deque()

    for d in range(4):
        nx, ny = hx + dx[d], hy + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if temp_route_map[nx][ny] > 0 and temp_route_map[nx][ny] < 4:
                if [nx, ny] not in tail:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    break

    while q:
        x, y = q.popleft()
        pp_group[tn] += 1
        my_team.append([x, y])

        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<= nx < n and 0<= ny<n and not visited[nx][ny]:
                if temp_route_map[nx][ny] > 0 and temp_route_map[nx][ny] < 4:
                    # 0 빈칸/ 1 머리사람 / 2 걍 사람  / 3 꼬리 사람 / 4 이동선
                    visited[nx][ny] = True
                    q.append([nx, ny])

    q = deque()
    tx, ty = my_team[-1]
    q.append([tx, ty])

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if temp_route_map[nx][ny] == 4:
                    # 0 빈칸/ 1 머리사람 / 2 걍 사람  / 3 꼬리 사람 / 4 이동선
                    my_team.append([nx, ny])
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return my_team

tnum = 0
visited = [[False]*n for _ in range(n)]
group = [[]]
tn = 1
for h in range(len(head)):
    if not head[h]:
        continue
    x, y = head[h]
    group.append(make_group(x, y, tn))
    tn += 1

###############
# 한 라운드
# 1. 각 팀은 머리사람을 따라 한칸 이동
def move_one(tn):
    global group

    group[tn] = [group[tn][-1]] + group[tn][:-1]
    return

# 3. 던져진 공에 사람이 있으면 최초로 만나게 되는 사람만이 공을 얻게 돼 점수를 얻음
# 2. 공이 정해진 선을 따라 던져짐,  n번째 라운드를 넘어가는 경우에는 다시 1번째 라운드의 방향으로 돌아갑니다.
def move_x(y, st, ed, move):
    global answer
    for x in range(st, ed, move):

        for g in range(1, m+1):
            my_group, pp = group[g], pp_group[g]
            if [x, y] in my_group[:pp]:
                for i in range(pp):
                    if group[g][i] == [x, y]:
                        answer += (i+1) ** 2
                        break
                group[g][:pp] = my_group[:pp][::-1]
                group[g][pp:] = my_group[pp:][::-1]

                return

def move_y(x, st, ed, move):
    global answer

    for y in range(st, ed, move):

        for g in range(1, m+1):
            my_group, pp = group[g], pp_group[g]
            if [x, y] in my_group[:pp]:
                for i in range(pp):
                    if group[g][i] == [x, y]:
                        answer += (i+1) ** 2

                        break
                group[g][:pp] = my_group[:pp][::-1]
                group[g][pp:] = my_group[pp:][::-1]

                return

#    머리 사람을 시작으로 k번째 사람이면 k**2만큼 점수 얻음

def shoot_ball(now):
    d = (now//n)%4 # now 1부터 시작

    if d == 0: #오른
        st = 0
        ed = n
        move = 1
        move_y(now%n, st, ed, move)

    elif d == 1: #위
        st = n-1
        ed = -1
        move = -1
        move_x(now%n,st, ed, move)

    elif d == 2: #왼
        st = n-1
        ed = -1
        move = -1
        move_y(n-1-now%n, st, ed, move)

    else: #아래
        st = 0
        ed = n
        move = 1
        move_x(n-1-now%n, st, ed, move)

answer = 0

for r in range(k):
    for tn in range(1, m+1):
        move_one(tn)

    shoot_ball(r)

print(answer)