"""
이전에 푼게 더 잘 푼 것 같다... 이전의 나만도 못 하다는 건가...
시간 : 522ms
공간 : 157MB
풀이 시간 : 4시간 20분
- 1시간 40분 즈음에 다 풀고 제출했는데, 웬걸....
- 디버깅 때문에 다 망했다. 심지어 이미 한번 푼 문제였는데...
- 이미 지나온 곳을 갈 수 없다고 생각했던 점이 모든 재앙의 시작점이었다.
- 팩맨 이동이 가장 어려운 함수이긴 했는데, 이렇게까지 헤멜것도 아니었다.
"""
GRID = 4
M, T = map(int, input().split()) # 몬스터의 수, 턴의 수


# 델타 배열
# 몬스터 -> 8방향, 반시계, ↑, ↖, ←, ↙, ↓, ↘, →, ↗
m_dr = [-1, -1, 0, 1, 1, 1, 0, -1]
m_dc = [0, -1, -1, -1, 0, 1, 1, 1]
# 팩맨 -> 상->좌->하->우
p_dr = [-1, 0, 1, 0]
p_dc = [0, -1, 0, 1]

# 팩맨
pac_r, pac_c = map(int, input().split()) # 팩맨 위치 입력
pac_r -= 1  # 행, 열 모두 1씩 빼줘야한다.
pac_c -= 1

# 몬스터
# 4 * 4 * [] 의 3차원 배열을 만든다.
monster = [[[] for _ in range(GRID)] for _ in range(GRID)]  # 몬스터의 방향을 저장한다. 위치 겹치기 가능
egg = [[[] for _ in range(GRID)] for _ in range(GRID)]  # 알의 방향을 저장한다. 위치 겹치기 가능
dead = [[0] * GRID for _ in range(GRID)]  # 시체의 남은 시간을 저장한다. 어차피 새로 생겼으면 걔 사라질 때 까지 기다려야한다.

# 몬스터 입력 받기
for _ in range(M):
    r, c, d = map(int, input().split())
    monster[r-1][c-1].append(d-1)  # 행, 열, 방향 입력 1씩 빼주고, 위치 겹침 가능이라 append로 한다.

# 입력처리 끝!


# 빠른 출력을 위한 함수
def print_grid():
    print("**************** 출력 ****************")
    print(f"팩맨 위치 : {pac_r}, {pac_c}")
    print("----- 몬스터 -----")
    for line in monster:
        print(*line)
    print()
    print("----- 알 -----")
    for line in egg:
        print(*line)
    print()
    print("----- 시체 -----")
    for line in dead:
        print(*line)
    print()


# 몬스터 복제후 알로 저장
def copy_monster():
    for r in range(GRID):
        for c in range(GRID):
            # 해당 위치의 몬스터들의 방향을 그대로 알에 저장한다.
            for m in monster[r][c]:
                egg[r][c].append(m)


# 몬스터 이동
def move_monster():
    moved = [[[] for _ in range(GRID)] for _ in range(GRID)]   # 이동한 몬스터를 저장해둘 배열이다.

    for r in range(GRID):
        for c in range(GRID):
            for m in monster[r][c]:
                stay = True  # 8방향 다 봤는데 못가면 다시 저장해야됨
                for d in range(8):
                    # 현재 위치(r, c)에서 현재 방향부터 갈 수 있는지 확인한다.
                    # 갈 수 없을 경우 반시계 45도 회전이다. 8개 다 돌았는데 못 가면 끝이다.
                    new_d = (m + d) % 8
                    new_r = r + m_dr[new_d]
                    new_c = c + m_dc[new_d]

                    # 문제에 제시된 갈 수 없는 3가지 조건
                    if not (0 <= new_r < GRID and 0 <= new_c < GRID):
                        continue
                    if new_r == pac_r and new_c == pac_c:
                        continue
                    if dead[new_r][new_c] > 0:
                        continue

                    # 갈 수 있는 경우, moved에 새 위치에 맞춰, 새 방향을 저장해준다.
                    stay = False
                    moved[new_r][new_c].append(new_d)
                    break

                # 8개를 다 봤는데 False가 안나온 경우
                if stay:
                    moved[r][c].append(m)

    # 이동한 몬스터들을 저장한다.
    for r in range(GRID):
        for c in range(GRID):
            monster[r][c] = moved[r][c][:]


# 팩맨 이동
def move_pacman():
    global pac_r, pac_c
    route = []
    # [디버깅] 99%에서 틀린 이유...🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫
    # 0으로 했다가, 팩맨이 몬스터를 한마리도 못 잡으면 움직이지 않게 되었다.
    max_eaten = -1
    # [계속 틀린 이유]🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫
    # 간 곳을 또 갈 수 있다, 물고기를 중복으로 먹지 않을 뿐
    visited = [[0] * GRID for _ in range(GRID)]
    # visited[pac_r][pac_c] = 1 <- 얘도 틀린 이유.

    # dfs로 루트 찾아옴. 근데 이 함수 내의 변수를 어떻게 가져다 쓰지?
    # 팩맨 경로 찾기
    def find_route(row, col, step, eaten):
        nonlocal max_eaten, route

        if len(step) == 3:
            if eaten > max_eaten:
                max_eaten = eaten
                route = step
            return

        # 상 -> 좌 -> 하 -> 우 순서로 돌아본다.
        for d in range(4):
            new_r, new_c = row + p_dr[d], col + p_dc[d]

            # 격자 밖은 논외
            if not (0 <= new_r < GRID and 0 <= new_c < GRID):
                continue
            if visited[new_r][new_c]:
                # [계속 틀린 이유]🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫🚫
                # 방문한 곳을 또 가면 중복 카운트다.
                # visited체크를 1, 0로만 하면 내가 원하지 않는 순간에 1이 0이 되어버린다.
                # 위 -> 아래 할 때 원래 위치가 0이 되어버린다.
                visited[new_r][new_c] += 1
                find_route(new_r, new_c, step + [d], eaten)
            else:
                visited[new_r][new_c] += 1
                find_route(new_r, new_c, step + [d], eaten + len(monster[new_r][new_c]))
            visited[new_r][new_c] -= 1

    find_route(pac_r, pac_c, [], 0)

    for d in route:
        pac_r += p_dr[d]
        pac_c += p_dc[d]

        # 팩맨이 도달한 위치에 있는 몬스터의 개수만큼, 2를 추가해줌.(시체가 사라질 시간 = 2)
        if monster[pac_r][pac_c]:
            dead[pac_r][pac_c] = 3
        # 몬스터 사망. 비워줌
        monster[pac_r][pac_c] = []


# 시체를 처리한다. 0 이상인 경우, 1을 감소시키고 다시 추가한다.
# 0이 되어버리면 추가 안하려고
def vanish_dead():
    for r in range(GRID):
        for c in range(GRID):
            if dead[r][c] > 0:
                dead[r][c] -= 1


# 알을 부화시킨다. 그냥 알을 다시 몬스터에 추가해준다.
def hatch_eggs():
    for r in range(GRID):
        for c in range(GRID):
            for e in egg[r][c]:
                monster[r][c].append(e)
            egg[r][c] = []


def solution():
    for _ in range(T):
        copy_monster()
        move_monster()
        move_pacman()
        vanish_dead()
        hatch_eggs()


    answer = 0
    for r in range(GRID):
        for c in range(GRID):
            answer += len(monster[r][c])

    print(answer)


solution()