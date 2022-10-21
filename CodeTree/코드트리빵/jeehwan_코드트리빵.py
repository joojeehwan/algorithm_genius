# 최단거리를 구할 수 있는 dfs, bfs 함수만 짜고 이어서 낼 풀기
# 근데 이거는 최단거리를 구하는거라 dfs보단 bfs가 맞아.

import sys
from collections import deque


#초기 입력

n, m  = map(int, input().split())

#초기 MAP 입력받기
MAP = [list(map(int, input().split())) for _ in range(n)]

'''

예시)

for num in range(n ** 2):

    #각 학생번호와 그 학생의 선호도 학생들이 번호로
    student = students[num]
    temp = []

    #완탐
    for row in range(n):
        for col in range(n):
            #일단 가지 않았 던 곳으로 가야한다.
            if not visited[row][col]:
                #자리를 선택하는 기준이 되는 선호도와 빈공간 counting
                like = 0
                blank = 0
                for k in range(4):
                    next_row = row + dr[k]
                    next_col = col + dc[k]

                    if 0 <= next_row < n and 0 <= next_col < n:
                        # 주위에 선호하는 학생이 있다면! 다 카운팅하기
                        if visited[next_row][next_col] in student[:] :
                            like += 1

                        if visited[next_row][next_col] == 0:
                            blank += 1

                temp.append([like, blank, next_row, next_col])

    #람다 관련해서 더 공부
    temp.sort(key = lambda x : (-x[0], -x[1], x[3], x[2]))
    #이제 실제 MAP에다가 넣기! 가장 맨 앞이 학생 번호 인 것.
    visited[temp[num][2]][temp[num][3]] = student[0]

'''
# 편의점 리스트 관리 , 이런식으로 굳이 이차원 배열의 형태로 관리 하지 않아 why?!
# 리스트에서 뽑아서, 람다의 형태로 우선순위를 관리 할꺼니깐!

#초기 편의점 입력 받는다!
cu_list = []

for _ in range(m):
    row, col = map(int, input().split())
    cu_list.append((row - 1, col - 1))

# bfs 함수 기록
visited = [[False] * n for _ in range(n)]

# 최단 거리 아아...!  아 이거 굳이 visited 배열로도 할 수 있다!

# 이 문제에서 이것을 쓴 이유는,
# 각 편의점별로(row, col)별로 가장 최단거리를 인덱스별로 기록하기 위힘
shortest = [[0] * n for _ in range(n)]

# 근데 원래 본디 나는 굳이 다른 메모리 써가면서 하지 않았음. 그냥 visted에다가 적으면서 했음.

visited_2 = [[0] * n for _ in range(n)]

# dx, dy값을
# 문제에서의 우선순위인 상좌우하 순으로 적어줍니다.
dr = [-1,  0, 0, 1]
dc = [ 0, -1, 1, 0]

#bfs 함수, 최단
def bfs(row, col):
    #만약에 visited 배열이 밖에 있엇다면, 굳이 이렇게 초기화를 하지 않아도 되었을 것
    for row in range(n):
        for col in range(n):
            visited[row][col] = False
            #viisted_2[row][col] = 0
            #shortest[row][col] = 0
    q = deque()
    q.append((row, col))
    visited[row][col] = True
    # visted_2[row][col] = 1
    # 그리고 아래 shortest는 없고
    #최단거리 갱신
    shortest[row][col] = 0

    while q :

        now_row, now_col = q.popleft()

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #범위 생각, 한번도 가보지 않은 곳.

            if 0 <= next_row < n and 0 <= next_col < n :
                #visited_2 의 처음을 0으로 두면, 아예 안 간 곳만 체크를 하게 된다. 
                if not visited[next_row][next_col] and MAP[next_row][next_col] != 2 :

                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    #visited_2[next_row][next_col] = visted_2[now_row][now_col] + 1
                    shortest[next_row][next_col] = shortest[now_row][now_col] + 1




from collections import deque

#상 좌 우 하
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(N)]
stores = [list(map(int, input().split())) for _ in range(M)]
# camp를 queue에 담기 및 관리
camp = deque()



