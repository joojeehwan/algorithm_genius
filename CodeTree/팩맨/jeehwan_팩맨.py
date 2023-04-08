

'''

문제 이해

4 * 4 격자에 m개의 몬스터와 1개의 팩맨이 주어짐.

몬스터 : 상하좌우 + 대각선(4방향)의 방향 중 하나를 가짐.

팩맨 : 상하좌우



아래의 턴 단위로 진행됨

1. 몬스터 복제 시도

> 현재위치에, 자신과 같은 방향을 가진 몬스터를 "알"의 형태로 복제 , 부화시에 동일한 자신을 복제한 몬스터와 같은 방향을 지니게 됨


2. 몬스터 이동

> 현재 자신이 가진 방향대로 한 칸 이동함.

>   팩맨이 있거나, 격자를 벗어나는 경우, 시체가 있음 => 반 시계 방향으로 45도 회전 한뒤 해당 방향으로 갈 수 있는지 판단.
    8방향 다 확인하는 동안 갈 수 없다고 판단되면 움직이지 않음


3. 팩맨 이동

> 총 3칸을 이동

> 상하좌우의 선택지

> 총 64가지의 선택지 코스 (4가지 방향 * 4가지방향 * 4가지방향) why 총 3칸을 이동

> 이중 가장 몬스터를 가장 많이 섭취할 수 있는 방향으로 이동

> 가장 많이 먹을 수 있는 경우가 여러개라면, "상 좌 하 우"의 방향으로 이동

> 이동하는 과정에 있는 몬스터만 먹는다(알, 움직이기 전에 함께 있던 몬스터)

??? 근데 움직이기 전에 함께 있는 몬스터가 있을 수 있나?! 초기에 그렇게 주어질 수 있는건가?!

> 팩맨에게 먹힌 몬스터는 시체를 남긴다.


4. 몬스터 시체 소멸

> 몬스터 시체가 소멸 되기 위해서는 2턴이 걸린다.



5. 몬스터 복제 완성

> 알 형태의 몬스터가 부화한다.


모든 턴이 진행한 후에 격자내에 살아있는 몬스터의 갯수를 구하시오


*참고*

함수로 뺴는 이유

1) 기능별로 나누기

2) return 을 사용해서, 더 이상의 반복없이 바로 반복문을 종료 하고 싶을 때 => 이게 더 큰 이유

'''

import copy

#몬스터 복제
def monster_copy():
    global grid
    return copy.deepcopy(grid)

# 몬스터가 갈 수 있는 8방향 조회
def next_pos(x, y, now_d):
    for c_d in range(8):
        nd = (now_d + c_d + 8) % 8
        nx, ny = x + dxs[nd], y + dys[nd]

        # 범위 안 , 시체 없고, 팩맨이 없는 경우
        if 1 <= nx < 5 and 1 <= ny < 5 and (nx, ny) != (px, py) and not graves[nx][ny]:
            return (nx, ny, nd)

    # 한바퀴 다돈 경우, 이동없이 원래 위치 반환
    return (x, y, now_d)


#몬스터 이동
def monster_move():
    global grid
    #몬스터 이동을 저장할 임시 배열 생성, 그 방향을 보고 있는 몬스터의 수
    new_grid = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(5)]

    for i in range(1, 5):
        for j in range(1, 5):
            for md in range(8):
                x, y, nd = next_pos(i, j, md)
                new_grid[x][y][nd] += grid[i][j][md]

    #원래 그리드에 몬스터의 이동 적용
    grid = copy.deepcopy(new_grid)



#팩맨 움직임
def packman_move():

    global px, py, grid
    result = -1
    result_route = []
    # print(px,py)

    # 가장 많이 먹는 경로 찾기
    # 해당 루트를 for문을 통해 순차적으로 넣는것만으로도,
    # 문제의 우선순위를 만족, why?! dr / dc를 그렇게 설정해둠.
    for route in packman_routes:

        nx, ny = px, py

        temp = 0
        # 정상 경로인지 확인
        flag = True

        #이동을 기록할 기록 배열
        visited = [[False for _ in range(5)] for _ in range(5)]

        #팩맨 이동 경로 인덱스(dir), 자연스레 3번의 움직임이 가능
        for pd in route:
            nx, ny = pdxs[pd] + nx, pdys[pd] + ny
            # 이동후 범위 생각

            # 격자 안으로 이동한 경우
            if 1 <= nx < 5 and 1 <= ny < 5:
                #한번 간곳 제외
                if visited[nx][ny]:
                    continue
                temp += sum(grid[nx][ny])
                visited[nx][ny] = True
            # 격자 밖으로 이동한 경우 새로운 경로
            else:
                flag = False
                #그 다음 route로 진행할 수 있도록 break
                break
        # 가장 많이 먹는 경우
        if flag and temp > result:
            result = temp
            result_route = route

    # 가장 많이 먹는 경로로 이동
    for pd in result_route:
        px, py = px + pdxs[pd], py + pdys[pd]

        # 방향 상관없는 그 격자내에 있는 모든 몬스터의 수
        if sum(grid[px][py]):
            # 방향을 고려해, 해당 격자의 몬스터의 수를 0 으로 처리, 팩맨에게 이미 먹혓으니
            for j in range(8):
                grid[px][py][j] = 0
            # 3을 할당하는 이유, 시체 3  => 2 1턴  // 2 => 1 1 턴 , 총 2턴
            # 3턴째 되는 경우부터 이동이 가능 해짐. 1 => 0 1턴 (3턴째)
            # 0이 되는 경우 next_pos에서  not 조건에 의해  True로 바뀌면서 이동이 가능해짐
            graves[px][py] = 3


# 시체의 턴 삭제
def remove_graves():
    for i in range(1, 5):
        for j in range(1, 5):
            if graves[i][j]:
                graves[i][j] -= 1


# 알 형태의 몬스터가 부화하는 부분 => 현재위치를 기록해, 그 몬스터의 수 만큼 더하면 그게 바로 알을 부화시키는 것
def monster_copy_done():
    for x in range(1, 5):
        for y in range(1, 5):
            for k in range(8):
                grid[x][y][k] += copied_monster[x][y][k]

# 팩맨 경로 구하기 (재귀함수를 통해 모든 경우의수 담기, 64가지)
# 이 번호는 차례대로 0부터 쌓이게 된다. 0 , 1 , 2가 순차적으로 
# 그렇다는 건 dr / dc를 문제의 우선순위에 맞게 적는다면, 
# 해당 번호들을 dr/dc에 넣는 것만으로도, 문제의 우선순위를 맞출 수 있어

def set_packman_routes(route):
    if len(route) == 3:
        packman_routes.append(route)
        return

    # 4방향으로 탐색이 가능.
    for i in range(4):
        set_packman_routes(route + [i])


# 그리드에 남아있는 몬스터의 수 카운팅
def count_monster():
    ans = 0
    for i in range(1, 5):
        for j in range(1, 5):
            ans += sum(grid[i][j])
    print(ans)


m, t = map(int, input().split())
px, py = map(int, input().split())
#격자만큼
graves = [[0 for _ in range(5)] for _ in range(5)]
# 방향의 몬스터 수
grid = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(5)]
packman_routes = []

for _ in range(m):
    r, c, d = map(int, input().split())
    grid[r][c][d - 1] += 1

# 몬스터 방향은 위 시작 반시계 (상 좌상 ,,, 우상)
dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
# 팩맨 방향은 상좌하우
pdxs, pdys = [-1, 0, 1, 0], [0, -1, 0, 1]

# 팩맨 경로 모두 구해두기
set_packman_routes([])

print(packman_routes)
# print("초기 몬스터")
# print(*grid,sep='\n',end='\n\n')
for _ in range(t):
    # 몬스터 복제
    copied_monster = monster_copy()

    # 몬스터 이동
    monster_move()
    # print("몬스터 이동")
    # print(*grid,sep='\n',end='\n\n')

    # 팩맨 이동
    packman_move()
    # print("팩맨 이동")
    # print(*grid,sep='\n',end='\n\n')

    # 몬스터 시체 소멸
    remove_graves()
    # print(*graves,sep='\n',end='\n\n')

    # 몬스터 복제 완성
    monster_copy_done()

    # print("몬스터 복제")
    # print(*grid,sep='\n',end='\n\n')

count_monster()






# 또 다른 풀이

# import copy
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
#
# def mons_move():
#     dx = [-1, -1, 0, 1, 1, 1, 0, -1]
#     dy = [0, -1, -1, -1, 0, 1, 1, 1]
#
#     res = [[[] for _ in range(n)] for _ in range(n)]
#     for x in range(n):
#         for y in range(n):
#             for d in live_mon[x][y]:
#                 check = False
#                 for i in range(9):
#                     nx, ny = x+dx[(d+i) % 8], y+dy[(d+i) % 8]
#                     if 0 <= nx < n and 0 <= ny < n and not dead_mon[nx][ny] and not (px == nx and py == ny):
#                         res[nx][ny].append((d+i) % 8)
#                         check = True
#                         break
#                 if not check:
#                     res[x][y].append(d)
#     return res
#
#
# def get_kiiled_num(d1, d2, d3):
#     x, y = px, py
#     s = 0
#     temp = []
#
#     for i in [d1, d2, d3]:
#         x, y = x+dx[i], y+dy[i]
#         if 0 <= x < n and 0 <= y < n:
#             if [x, y] not in temp:
#                 s += len(live_mon[x][y])
#                 temp.append([x, y])
#         else:
#             return -1
#     return s
#
#
# def pack_move():
#     global px, py
#
#     # best 경로 설정
#     MAX, path = -1, (-1, -1, -1)
#     for i in range(4):
#         for j in range(4):
#             for k in range(4):
#                 num = get_kiiled_num(i, j, k)
#                 if num > MAX:
#                     MAX = num
#                     path = (i, j, k)
#
#     # 몬스터 시체 소멸.
#     for i in range(n):
#         for j in range(n):
#             temp = []
#             for dead in dead_mon[i][j]:
#                 cnt = dead-1
#                 if cnt > 0:
#                     temp.append(cnt)
#             dead_mon[i][j] = temp
#
#     # 팩맨 이동.
#     for i in path:
#         px, py = px+dx[i], py+dy[i]
#         if live_mon[px][py]:
#             live_mon[px][py] = []
#             dead_mon[px][py].append(2)
#
#
# def dupl_comp():
#     for i in range(n):
#         for j in range(n):
#             if dupl_mon[i][j]:
#                 for d in dupl_mon[i][j]:
#                     live_mon[i][j].append(d)
#
#
# m, t = map(int, input().split())
# px, py = map(int, input().split())
# px, py = px-1, py-1
# n = 4
# live_mon = [[[] for _ in range(n)] for _ in range(n)]
# dead_mon = [[[] for _ in range(n)] for _ in range(n)]
# for _ in range(m):
#     mx, my, d = map(int, input().split())
#     live_mon[mx-1][my-1].append(d-1)
# for _ in range(t):
#     dupl_mon = copy.deepcopy(live_mon)
#     live_mon = mons_move()
#     pack_move()
#     dupl_comp()
#
# ans = 0
# for i in range(n):
#     for j in range(n):
#         if live_mon[i][j]:
#             ans += len(live_mon[i][j])
#
# print(ans)


