'''

회전하는 빙하

마법사상어와 파이어 스톰이랑 같은 문제


<문제 이해>

1. 2**n * 2 **n 격자

2. 2** L * 2 ** L 격자를 선택하여, 2 ** (L -1) * 2 ** (L - 1)만큼 잘라 4등분 시계방향 회전

    - 회전 레벨이 0인 경우는 회전이 존재하지만, 회전이 일어나도 각각의 얼음의 위치는 변하지 않음.
    =>아무 변화 없다고 생각.

3. 빙하의 회전이 끝난 후 녹기 진행

    - 얼음이 녹는 것은 "똥시에" 진행
    
    - IF 인접(상하좌우)에 얼음이 3개 이상 : 
        THEN, 녹지 않음. 
      ELSE :
        1이 줄어듬

    - 격자를 벗어나는 경우 / 해탕 칸의 값이 0인 경우 => 얼음 존재X
    
4. "회전 -> 녹기 " 가 끝난 후에 가장큰 얼음의 군집 크기 & 방하의 총양 출력

    - 얼음의 군집 크기 : 연결된 칸의 집합

    - 빙하의 총양 : 격자에 숫자들의 총합

'''


import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


#하 우 상 좌 => 도는 방향과 연관이 되어 있다.
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

#데이터 입력받기
n, q = map(int,  input().split())
n = 2 ** n
MAP = [list(map(int, input().split())) for _ in range(n)]
levels = list(map(int, input().split()))
#빙하 세기
ans = 0
cnt = 0

#DFS VERSION
def dfs(row, col):
    global ans
    ret = 1 #1씩 계속 더해져서, 결국 그 개수를 counting하게 된다.
    MAP[row][col] = 0 #이미 센곳이라 0으로

    for dir in range(4):

        next_row = row + dr[dir]
        next_col = col + dc[dir]

        #범위체크, 얼음 없는 곳 안간다

        if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col]:
            ret += dfs(next_row, next_col)

    ans = max(ans, ret)
    return ret

#BFS VERSION
def bfs(row, col):

    q = deque()
    q.append((row, col))
    MAP[row][col] = 0
    global cnt
    cnt = 1

    while q :
        now_row, now_col = q.popleft()
        for k in range(4):
            next_row = now_row + dr[k]
            next_col = now_col + dc[k]

            #범위생각, 얼음 없는 곳 안가
            if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col]:
                cnt += 1
                q.append((next_row, next_col))
                #여기도 지금 간 곳이니깐, 다음 counting에서 빼야 한다.
                MAP[next_row][next_col] = 0

    return cnt

# 1 2
for level in levels:

    if level == 0:
        continue

    k = 2 ** level
    # 회전


    # 단계에 맞게, 주어진 2차원 배열을 좌상단부터 쪼갠다.
    # 그리고 회전까지
    for row in range(0, n, k):
        for col in range(0, n, k):
            debug = 1
            temp = []
            #해당 범위에 있는 것들
            for i in range(row, row + k):
                temp.append(MAP[i][col:col + k])

            #temp 배열을 활용한 90도 회전

            for i in range(k):
                for j in range(k):
                    MAP[row + j][col + k - 1 - i] = temp[i][j]


iceCnt = [[0] * n for _ in range(n)]

#완전탐색을 하는 것
for row in range(n):
    for col in range(n):

        for dir in range(4):

            next_row = row + dr[dir]
            next_col = col + dc[dir]

            #범위 체크 & 얼음이 있으면(0 초과)
            if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] > 0 :
                iceCnt[row][col] += 1


#기록을 바탕으로 그 이후에, 빙하 삭제

for row in range(n):
    for col in range(n):
        if MAP[row][col] > 0 and iceCnt[row][col] < 3:
            MAP[row][col] -= 1

print(sum(sum(i) for i in MAP))

for row in range(n):
    for col in range(n):

        if MAP[row][col] > 0:
            ans = max(ans, bfs(row, col))
            #dfs(row,col)

print(ans)


'''

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

#하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


#데이터 입력받기

n, q = map(int, input().split())
n = 2 ** n
MAP = [list(map(int, input().split())) for _ in range(n)]
l = list(map(int, input().split()))

# print(l)
visited = [[False] * n for _ in range(n)]
ans = 0
cnt = 0

def dfs(row, col):
    global ans
    ret = 1 #개수 counting
    # visited[row][col] = True
    MAP[row][col] = 0
    for dir in range(4) :
        next_row = row + dr[dir]
        next_col = col + dc[dir]

        #범위 체크, 한번도 가지 않은 곳 + 얼음 없는 곳은 가지 않아.
        if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] :
            ret += dfs(next_row, next_col)
    #가장 큰 덩어리가 차지하는 칸의 개수이니..!
    ans = max(ans, ret)
    return ret

for L in l:

    k = 2 ** L
    # l의 단계에 맞게, 격자 나누기 => 이게 제일 어렵다.
    for row in range(0, n, k):
        for col in range(0, n, k):
            temp = []
            for i in range(row, row + k):
                temp.append(MAP[i][col:col + k])
            # print(temp)

            #회전
            for i in range(k):
                for j in range(k):
                    MAP[row + j][col + k - 1 - i] = temp[i][j]

    # print(MAP)

    #근처 얼음 counting 그 이후에 제거 (세는 것과 녹이는 것을 동시에 할 수 없다.)
    iceCnt = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            for dir in range(4):
                next_row = row + dr[dir]
                next_col = col + dc[dir]

                #범위 체크 & 얼음이 있으면
                if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] :
                    iceCnt[row][col] += 1

    for row in range(n):
        for col in range(n):
            if MAP[row][col] > 0 and iceCnt[row][col] < 3:
                MAP[row][col] -= 1

print(sum(sum(i) for  i in MAP))

for row in range(n):
    for col in range(n):
        if MAP[row][col] > 0 :
            dfs(row, col)

print(ans)


'''





