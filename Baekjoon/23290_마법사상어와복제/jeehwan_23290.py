'''


4 x 4 크기의 격자에서 이루어짐.

- 물고기 M마리가. 격자의 칸 하나에 한 마리씩 들어가 있음.(둘 이상의 물고기가 같이 있을 수도, 마법사 상어랑 같이 있을 수도)
각 물고기는 이동 방향(상하좌우 + 대각선 8방향)을 가지고 있음

- 상어(마법사)도 격자에 들어가서, 칸 하나를 차지 함.(Sx, Sy // 입력의 마지막 것들)

- 아래와 같은 순서로 s번 연습

<복제 마법 순서>

1) 모든 물고기에 복제 마법을 시전, 시간이 걸려서 5번 step에서 이루어짐

2) 모든 물고기가 한 칸 이동, 그러나 상어가 있는 칸, 물고기의 냄사가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동x

   각 물고기는, 자신이 가지고 있는 이동방향이 이동할 수 있는 향할 떄 까지 45도 반 시계 회전

   만약, 이동할 수 없다면 이동x

3) 상어가 연속해서 3칸 이동.(상 하 좌 우) 인접한 칸으로 이동. 단) 격자 범위 안에서,

   물고기를 만나면, 그 칸에 있는 모든 물고기는 제외

   제외 되면 => 냄새를 남김.

   가능한 이동 방법 중에서, 제외되는 물고기의 수가 가장 많은 방법으로 이동(그러한 방법이 여러개?! 사전순으로)

=> 8방향을 정수로 표현('좌'부터 '좌하' 까지 1 ~ 8)

4) 물고기의 냄새는 2회만 지속됨. 3번 째 부터는 유효하지 않고 사라짐


5) (1)에서 시행한 복제마법이 완료됨.



<구현해야 하는 함수>

1. 물고기 움직이게 하는 함수

2. 상어 이동 dfs => 그 위치 기준으로 제외되는 물고기가 얼마나 많은지 완전 탐색



'''
import copy

def move_fish():
    """
    물고기 이동
    1. 상어가 있는 칸, 물고기 냄새 칸, 벗어나는 칸 x
    2. 45도 반시계 회전 후 이동. 이동 못하는 경우 그대로
    :return:
    """
    res = [[[] for _ in range(4)] for _ in range(4)]


    #그 곳에 물고기가 있다면?! => 이동방향이 있는 곳을 찾기위해 완전탐색 도는 것.
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                # for문과 같이 사용되는 else문은 for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우
                # else문이 실행되는 방식으로 진행됨.
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    # 3가지 조컨 case 거르기 (상어 칸, 냄새 칸, 격자 밖)
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    #어디도 갈곳이 없네?! 위에서 pop했던 것 다시 넣어두자.
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, cnt, visit):
    """
    상어 3칸 이동
    1. 제외되는 물고기 수가 많고 > 이동방법 사전순(백트래킹하면 자동으로 됨)
    2. 이동한 곳을 저장 > 물고기 냄새가 됨
    """
    global max_eat, shark, eat
    if dep == 3:   # 3번 이동한 경우 그만, 가장 많은 물고기를 제외하기 위해서, cnt로 최댓값, 상어의 위치 기억하고, 상어의 이동을 기록
        if max_eat < cnt:
            max_eat = cnt
            shark = (x, y)
            eat = visit[:]
        return
    #상어 이동 4방향 가능 하니깐
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:  # 처음 방문, cnt에 죽은 물고기 수 추가
                visit.append((nx, ny))
                dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
                visit.pop()
            else:  # 방문한 경우
                dfs(nx, ny, dep + 1, cnt, visit)

#       ←, ↖,   ↑,  ↗, →, ↘, ↓, ↙
f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
# 이동방향을 [] 안에다가 넣는다.
graph = [[[] for _ in range(4)] for _ in range(4)]

for x, y, d in fish:
    graph[x - 1][y - 1].append(d - 1)

# 상어의 좌표에서 바로 -1 한채로 입력을 받고 싶어서, 람다(익명함수)를 이용해서 입력받음.
shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0] * 4 for _ in range(4)]

for _ in range(s):
    eat = list()
    max_eat = -1
    # 1. 모든 물고기 복제
    temp = copy.deepcopy(graph)
    # 2. 물고기 이동
    temp = move_fish()
    # 3. 상어이동 - 백트래킹
    dfs(shark[0], shark[1],0, 0, list())
    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3   # 3번 돌아야 없어짐
    # 4. 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1
    # 5. 복제 마법
    for i in range(4):
        for j in range(4):
            graph[i][j] += temp[i][j]

# 물고기 수 구하기
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(graph[i][j])

print(answer)


# 1
# print(-1 % 8) # 값이 양수 7 나온다.


# 2
# https://stackoverflow.com/questions/44714705/python-access-global-list-in-function
# 복사할 때는, global로 해서 가져와야 한다.

def func(lst):
    res = []
    #global test
    #global로 가져오면 여기서 또 에러 나네
    test[0] = 1

    #밑에 복사가 들어가면, 오류가 난다. ... 왜그러는걱지?!
    #test = lst[:]

    return res

test = []
temp = func([1,2,3,4,5])

