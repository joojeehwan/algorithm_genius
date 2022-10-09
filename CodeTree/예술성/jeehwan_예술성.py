'''

예술성

n은 반드시 홀수
'''
from collections import deque

#초기 입력 및 세팅

n = int(input())

MAP = [list(map(int, input().split())) for _ in range(n)]

temp = [[0] * n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#각 칸의 그룹번호를 적어둔다.
group = [[0] * n for _ in range(n)]

# 그룹의 개수 관리
group_n = 0

# 각 그룹마다 칸의 수를 세기
# => 나올 수 있는 그룹의 전체 가짓수 n * n 이니, + 1 을 해서 절대 인덱스 에러가 안나도록.
group_cnt = [0] * (n * n + 1)

#기록 배열
visited = [[False] * n for _ in range(n)]


# bfs (그룹의 개수 counting) // dfs로도 해보기 함수
def bfs(row, col):

    #visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((row, col))
    visited[row][col] = True

    while q:

        now_row, now_col = q.popleft()
        
        for k in range(4):
            
            next_row = now_row + dr[k]
            next_col = now_col + dc[k]
            
            #범위
            if 0 <= next_row < n and 0 <= next_col < n:
                if not visited[next_row][next_col] and (MAP[now_row][now_col] == MAP[next_row][next_col]):
                    visited[next_row][next_col] = True
                    group[next_row][next_col] = group_n
                    group_cnt[group_n] += 1
                    q.append((next_row, next_col))


# 그룹 구분짓기 함수

def make_group():
    global group_n

    group_n = 0
    # 그냥 bfs 안에 visited 배열이 있었으면 굳이 초기화 안해도 되지만!
    # 전역으로 visited를 관리하기 때문에 초기화 작업이 필요 함.
    for row in range(n):
        for col in range(n):
            visited[row][col] = False

    for row in range(n):
        for col in range(n):
            if not visited[row][col] :
                group_n += 1
                group[row][col] = group_n
                group_cnt[group_n] = 1
                bfs(row, col)

# 점수 counting 함수

def get_score() :
    johwa_score = 0

    #"특정 변"을 사이에 두고, 두 칸의 그룹이 다르다면
    # 즉, 각 칸 마다 인접(상하좌우)한 곳에 다른 그룹의 칸이 있다면! 
    # 즉, 각 칸 검사해서, 인접한 곳에 다른 그룹의 칸이 있는지 알아봐라
    for row in range(n):
        for col in range(n):
            #각 칸마다 검사
            for k in range(4):
                next_row = row + dr[k]
                next_col = col + dc[k]

                if 0 <= next_row < n and 0 <= next_col < n :
                    if MAP[row][col] != MAP[next_row][next_col] :
                        group1 = group[row][col]
                        group2 = group[next_row][next_col]
                        group1_cnt, group2_cnt = MAP[row][col], MAP[next_row][next_col]
                        cnt1, cnt2 = group_cnt[group1], group_cnt[group2]

                        johwa_score += (cnt1 + cnt2) * group1_cnt * group2_cnt


    return johwa_score // 2



#정사각형 시계방향으로 90도 회전
'''

새로운 배열을 이용해서 회전을 하게 되면...!

그냥 하나로만 해서, 생각했을 때랑 반대가 된다. 

상상하기를 2개의 판이 있는데, 뒤에 있는 판은 반시계 하는 건

결국 앞에 있는 판을 시계로 돌려서 찍는거랑 같은 거자나?!

그런 원리! 

MAP은 그대로 두고!(원본의 인덱스는 그대로 row, col 이고)

'''
# 회전
def rotate_square(start_row, start_col, square_n):

   for row in range(start_row, start_row + square_n) :
       for col in range(start_col, start_col + square_n):
            
            #(0, 0)으로 가져와서 변환 진행
            o_row, o_col = row - start_row, col - start_col
                
            #좌표 변환
            r_row, r_col = o_col, square_n - o_row - 1

            #다시 원래 좌표로
            temp[r_row + start_row][r_col + start_col] = MAP[row][col]


def rotate() :

    #temp 배열 초기화
    for row in range(n):
        for col in range(n):
            temp[row][col] = 0
    # 회전을 진행
    
    # 1 십자 모양 회전

    for row in range(n):
        for col in range(n):
            if row == n // 2:
                temp[n - col -1][row] = MAP[row][col]

            elif col == n // 2:
                temp[col][row] = MAP[row][col]

    # 2 사각형 회전
    sqaure_n = n // 2
    rotate_square(0, 0, sqaure_n)
    rotate_square(0, sqaure_n + 1, sqaure_n)
    rotate_square(sqaure_n + 1, 0, sqaure_n)
    rotate_square(sqaure_n + 1, sqaure_n + 1, sqaure_n)
    
    # temp 값을 다시 적용
    for row in range(n):
        for col in range(n):
            MAP[row][col] = temp[row][col]
    


#전체 시뮬레이션 3회 반복(1 - 3 회의 예술점수를 모두 합한 값을 출력)


ans = 0

for _ in range(4):
    # 그룹 생성
    make_group()
    # 예술 점수 계산
    art_score = get_score()
    ans += art_score
    # 회전
    rotate()

print(ans)