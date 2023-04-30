'''

격자 크기 n(3 ≤ n ≤ 20), 팀의 개수 m(1 ≤ m ≤ 5), 라운드 수 k(1 ≤ k ≤ 1000)

0 빈칸

1 머리 사람

2 머리x 꼬리x

3 꼬리 사람

4 이동 선

이동선은 반드시 2개의 인접한 칸에만 존재,
하나의 이동 선에는 하나의 팀만이 존재 한다.

dfs / bfs 두 가지 방법 모두로 풀어보기

'''

# test = [[1,2,3], [1]]
# test[0].append((4, 5))
# print(test[0])

# 초기 입력 및 세팅

n, m, k = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

''' 
각 팀별 레일 위치를 관리 => MAP을 형상화 한 것이 아님. 즉, 팀 IDX 마다 그 팀에 해당하는 (row col) 을 담기 위함.
ex) [[(0, 0), (0, 1)], [(2, 0), (3, 0)]] 

=> idx 0 번 팀은 레일 (0, 0), (0, 1)을 따라 간다.
=> idx 1 번 팀은 레일 (2, 0), (3, 0)을 따라 간다. 

'''
# 각 팀별 레일 위치를 기록
rail = [[] * n for _ in range(n)]

# 각 팀 별 tail의 위치를 관리
tail = [0] * (m)

#for dfs
visited = [[False] * n for _ in range(n)]

#격자 내 레일에 각 팀 번호를 적어둔다. 
MAP_idx = [[0] * n for _ in range(n)]

#정답
ans = 0

#델타 배열 (상 하 좌 우)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


#초기 레일을 만들기 위해 dfs를 이용
'''
머리 부터 dfs를 시작하고, 그 다음엔 통로로만 dfs를 이동하게 하니
자연스레 팀이 있는 곳으로만 가게 된다. 
따라서 자연스레 rail[i]에 머리부터 팀원, 그리고 그냥 통로가 순서대로 담겨서
점수를 계산할 때, index로 바로 뽑아서 몇번 째 팀원이 공에 맞았는지 확인 가능
'''
def dfs(row, col, idx):
    #idx는 팀의 번호
    visited[row][col] = True
    MAP_idx[row][col] = idx

    for k in range(4):
        next_row = row + dr[k]
        next_col = col + dc[k]

        # 범위 체크
        if 0 <= next_row < n and 0 <= next_col < n :
            # 조건 (이미 간 곳이나, 레일의 경로가 아니면 넘어간다)
            if visited[next_row][next_col] or MAP[next_row][next_col] == 0 :
                continue
                
            # 가장 처음 탐색을 할 때, 2가 있는(머리도 꼬리도 아닌) 방향으로 dfs 진행
            if len(rail[idx]) == 1 and MAP[next_row][next_col] != 2:
                continue

            rail[idx].append((next_row, next_col))

            #꼬리 사람이면!? 머리로부터 몇 번째 꼬리인지 기록
            if MAP[next_row][next_col] == 3:
                tail[idx] = len(rail[idx])

            dfs(next_row, next_col, idx)

def init():

    cnt = 0

    # 초기 MAP을 rail에 기록하기, 머리 사람을 우선 앞에 넣어주기
    for row in range(n):
        for col in range(n):

            #머리 사람
            if MAP[row][col] == 1 :
                rail[cnt].append((row, col))
                cnt += 1

        # dfs를 통해서, MAP을 순서대로 rail에 넣어준다.

    for i in range(m):
        #[i][0]을 하는 이유는 각 팀의 레일마다, 하나의 레일(머리사람)만 넣어서 dfs를 돌리니깐
        row, col = rail[i][0]
        dfs(row, col, i)

    debug = 1

# 각 팀을 이동시키는 함수 => 이 함수 기록
# 굳이 맨 마지막 인덱스를 기록하는 것, 시험 해보기
def all_move() :

    for i in range(m):
    # 각 팀에 대해 레일을 한 칸씩 머리방향으로 이동
    # temp => 머리 기준 바로 뒤에 있는 레일 한칸(row, col)을 선택
        temp = rail[i][-1]


        debug = 1

        for j in range(len(rail[i]) -1, 0, -1):
            #한 칸씩 이동
            rail[i][j] = rail[i][j - 1]
        #가장 뒤에 있는 것을 가장 앞으로 꺼내
        rail[i][0] = temp

    #백터에 저장한 정보를 바탕으로 보드의 표기도 바꿔준다.
    #tail[idx]에 꼬리 기준으로 앞으로 몇명이나 있는지 정보가 있어서
    #아래와 같은 if문 분기가 가능한 것
    for i in range(m):
        for j, (row, col) in enumerate(rail[i]):
            # 머리 사람
            if j == 0:
                MAP[row][col] = 1
            #머리X 꼬리X
            elif j < tail[i] - 1 :
                MAP[row][col] = 2
            #꼬리
            elif j == tail[i] - 1 :
                MAP[row][col] = 3
            #이동선
            else:
                MAP[row][col] = 4
                
# (row, col) 지점에 공이 닿았을 때의 점수를 계산
def get_score(row, col):
    global ans
    idx = MAP_idx[row][col]
    #(row, col)이 몇번째에 있는데 맞았는가?!
    cnt = rail[idx].index((row, col))
    ans += (cnt + 1) * (cnt + 1)


# trun 번째 라운드의 공을 던짐
# 공을 던졌을 때 이를 받은 팀의 번호를 반환
def throw_ball(turn):
    #라운드 모듈러 연산
    t = (turn) % (4 * n) + 1

    #가로(좌 -> 우)
    if t <= n:

        # 1 ~ n 라운드의 경우 왼쪽에서 오른쪽으로 공을 던짐
        for i in range(n):
            if 1 <= MAP[t][i] and MAP[t][i] <= 3:
                #사람이 있는 첫번쨰 지점을 확인
                #찾게 되면, 점수를 계산하고, 공과 맞은 팀의 번호를 반환
                get_score(t, i)
                return MAP_idx[t][i]

    # 세로(하 -> 상)
    elif t <= 2 * n:

        t -= n
        # n + 1 ~ 2n 라운드의 경우 아래에서에서 윗 쪽으로 공을 던짐
        for i in range(n):
            #인덱스를 조정해서 아래에서 위로 가게 끔 확인
            if 1 <= MAP[n + 1 - i][t] and MAP[n + 1 - i][t] <= 3:
                # 사람이 있는 첫번쨰 지점을 확인
                # 찾게 되면, 점수를 계산하고, 공과 맞은 팀의 번호를 반환
                get_score(n + 1 - i, t)
                return MAP_idx[n + 1 - i][t]
    #가로(우 -> 좌)
    elif t <= 3 * n:

        t -= (2 * n)
        # 2n + 1 ~ 3n 라운드의 경우 아래에서에서 윗 쪽으로 공을 던짐
        for i in range(n):
            #인덱스를 조정해서 오른쪽에서 왼쪽으로 가게 끔 확인
            if 1 <= MAP[n + 1 - t][n + 1 - i] and MAP[n + 1 - t][n + 1 - i] <= 3:
                # 사람이 있는 첫번쨰 지점을 확인
                # 찾게 되면, 점수를 계산하고, 공과 맞은 팀의 번호를 반환
                get_score(n + 1 - t, n + 1 - i)
                return MAP_idx[n + 1 - t][n + 1 - i]

    #세로(상 -> 하)
    else:
        t -= (3 * n)
        #3n + 1 ~ 4n 라운드의 경우 위에서 아래쪽으로 공을 던짐
        for i in range(n):
            # 인덱스를 조정해서 오른쪽에서 왼쪽으로 가게 끔 확인
            if 1 <= MAP[i][n + 1 - t] and MAP[i][n + 1 - t] <= 3:
                # 사람이 있는 첫번쨰 지점을 확인
                # 찾게 되면, 점수를 계산하고, 공과 맞은 팀의 번호를 반환
                get_score(i, n + 1 - t)
                return MAP_idx[i][n + 1 - t]

    #공이 그냥 지나가면 0을 반환
    return 0


#공을 획득한 팀 순서 바꾸기 "머리 사람" , "꼬리 사람" 위치 change
def reverse(got_ball_idx):

    #아무도 공 못받았으면 넘어가기
    if got_ball_idx == 0:
        return

    idx = got_ball_idx

    new_rail = []

    #순서에 맞춰서 new_rail에 레일을 넣어준다.
    #일단 진짜 사람들 부터(뒤에 있는 꼬리부터 넣고 순서대로 머리까지, 이제 머리가 꼬리가 되지)
    for j in range(len(tail[idx]) - 1, -1, -1):
        new_rail.append(rail[idx][j])
        
    #그 다음 경로들, 이것도 마찬가지로 뒤에서 부터 넣어준다. 원래의 순서를 유지하면서 딱 방향만 바뀌도록
    for j in range(len(rail[idx] - 1, tail[idx] - 1, -1)):
        new_rail.append(rail[idx][j])

    rail[idx] = new_rail[:]

    #실제 MAP도 바꾼다.
    for j, (row, col) in enumerate(rail[idx]):
        if j == 0:
            MAP[row][col] = 1
        elif j < tail[idx] - 1 :
            MAP[row][col] = 2
        elif j == tail[idx] - 1 :
            MAP[row][col] = 3
        else:
            MAP[row][col] = 4

init()
for i in range(k):

    all_move()

    got_ball_idx = throw_ball(i)

    reverse(got_ball_idx)

print(ans)


