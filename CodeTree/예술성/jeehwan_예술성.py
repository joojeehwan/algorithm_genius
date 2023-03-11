'''
예술성 20220311

1. n * n 격자에 그려져 있는 그림

2. 각 칸의 색깔을 1 이상 10이하의 숫자로 표현

3. 동일한 숫자가 상하좌우로 인접해 있는 경우, 동일한 그룹으로 판단

    - 예술 점수는 모든 그룹 쌍의 조화로움의 합으로 정의가 됨.

    - 그롭 a 와 그룹 b의 조화로움

    => (그룹 a 에 속한 칸의 수 + 그룹 b에 속한 칸의 수) * 그룹 a를 이루고 있는 숫자 값 * 그룹 b를 이루고 있는 숫자 값 * "그룹 a와 b가 서로 맞닿아 있는 변의 수"


4. 그룹 쌍 간의 조화로움 값이 0보다 큰 조합들의 합을 전부 더해 "초기 예술 점수"를 구함.

5. "초기 예술 점수"를 구한 다음에는 그림에 대한 2개의 회전을 동시에 진행

    - 십자 모양의 경우, 십자의 중심은 그대로 있고, 나머지들이 통째로 반시계 방향으로 90도 회전

    - 십자 모양을 제외한, 나머지 4개의 정사각형 부분은 개별적으로 시계방향으로 90도 회전


6. 이렇게 5번의회전을 n회 진행 한 후 구한 예술 점수를 "n회전 이후 예술 점수" 라고 함.

7. 초기 예술 점수, 1회전 후 예술 점수, 2회전 후 예술 점수, 3회전 이후 예술 점수의 합을 구하라


입력

첫 번째 줄에 n이 주어집니다. n은 반드시 "홀수"입니다.
이후 n개의 줄에 걸쳐 각 행에 칠해져 있는 색깔에 대한 정보인 숫자들이 공백을 사이에 두고 주어집니다.

3 ≤ n ≤ 29
1 ≤ 주어지는 숫자 ≤ 10

출력

첫 번째 줄에 초기 예술 점수, 1회전 이후 예술 점수, 2회전 이후 예술 점수, 그리고 3회전 이후 예술 점수를 모두 합한 값을 출력

'''


from collections import deque

#초기 입력 및 세팅

n = int(input())

MAP = [list(map(int, input().split())) for _ in range(n)]

#동시에 변화하는 회전을 한번에 MAP에 적용하기 위한 임시 배열
temp = [[0] * n for _ in range(n)]

#델타 배열 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#각 칸의 그룹번호를 적어둔다.
group = [[0] * n for _ in range(n)]

# 그룹의 개수 관리
group_n = 0

# 각 그룹마다 칸의 수를 세기
# => 나올 수 있는 그룹의 전체 가짓수 n * n 이니, + 1 을 해서 절대 인덱스 에러가 안날 수 있도록 함.
group_cnt = [0] * (n * n + 1)

#기록 배열 for bfs
visited = [[False] * n for _ in range(n)]

# bfs (그룹의 개수 counting) // dfs로도 해보기 함수
def bfs(row, col):

    #visited = [[False] * n for _ in range(n)]
    q = deque() # 큐 생성
    q.append((row, col)) #초기값 세팅
    visited[row][col] = True #visted 배열 체크

    #while문을 통해, bfs 시작
    while q: # q안에 값이 있는 동안 아래의 로직 수행

        #q에서 값 꺼내기
        now_row, now_col = q.popleft()

        #4방향으로 이동 => 인접한 4방향
        for k in range(4):

            #다음 방향으로 아동
            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            #이동 후 범위 체크
            if 0 <= next_row < n and 0 <= next_col < n:
                # 한번도 가지 않은 곳 이면서, 현재 그룹의 번호와 값은 것들만 => 그룹화를 하기 위함
                if not visited[next_row][next_col] and (MAP[now_row][now_col] == MAP[next_row][next_col]):
                    visited[next_row][next_col] = True
                    # 각 칸의 그룹 번호를 기록함
                    group[next_row][next_col] = group_n
                    # 그룹번호를 인덱스로 하여, 몇 번 그룹이 몇개의 칸의 범위를 차지하고 있는지 기록 for 조화로움 계산시 사용
                    group_cnt[group_n] += 1
                    # 다음 bfs를 위한 q 추가
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

    #
    for row in range(n):
        for col in range(n):
            if not visited[row][col] :
                group_n += 1 #0번 그룹은 없으니 1번 그룹부터 할당
                # bfs함수안에서 할당해주지 못하는 초기값 할당
                group[row][col] = group_n
                group_cnt[group_n] = 1
                # bfs 시작
                bfs(row, col)

# 점수 counting 함수

def get_score() :
    johwa_score = 0

    # "특정 변"을 사이에 두고, 두 칸의 그룹이 다르다면
    # 즉, 각 칸 마다 인접(상하좌우)한 곳에 다른 그룹의 칸이 있다면!
    # 즉, 각 칸 검사해서, 인접한 곳에 다른 그룹의 칸이 있는지 알아봐라

    # 각, 칸마다 검사
    for row in range(n):
        for col in range(n):
            # 인접한 곳으로 이동
            for k in range(4):
                next_row = row + dr[k]
                next_col = col + dc[k]
                #항상 이동후 범위 체크
                if 0 <= next_row < n and 0 <= next_col < n :
                    #현재 내가 있는 곳의 그룹번호와 다른 그룹번호가 이동후 발견되었다면?!
                    if MAP[row][col] != MAP[next_row][next_col] :

                        group1 = group[row][col]
                        group2 = group[next_row][next_col]
                        group1_cnt, group2_cnt = MAP[row][col], MAP[next_row][next_col]
                        cnt1, cnt2 = group_cnt[group1], group_cnt[group2]

                        johwa_score += (cnt1 + cnt2) * group1_cnt * group2_cnt


    # 중복으로 계산했으니, // 2로 나누어 점수 계산
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



def rotate():
    global MAP
    # temp 배열 초기화
    for row in range(n):
        for col in range(n):
            temp[row][col] = 0
    # 회전을 진행

    # 1 십자 모양 회전

    for row in range(n):
        for col in range(n):
            if row == n // 2:
                temp[n - col - 1][row] = MAP[row][col]

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

    # 이건 전역으로 안 쓸때만 사용이 된다.
    # MAP = temp[:]

    # 전체 시뮬레이션 3회 반복(1 - 3 회의 예술점수를 모두 합한 값을 출력)

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