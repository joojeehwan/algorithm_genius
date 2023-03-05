'''

완전탐색

- N x M 크기의 MAP

- MAP위의 3가지 종류의 경우의 수  :

    1. 동전(2개) : o

    2. 빈 칸 : .

    3. 벽 : #

- 버튼(왼, 오, 위, 아래)을 사용해, MAP위의 동전(2개)이 동시에 움직임.

- 동전 이동 규칙

    1. 이동하려는 칸이 벽이면 동전은 이동X

    2. 이동하려는 방향에 칸이 없으면, 동전은 보드 바깥으로 떨어짐(MAP을 벗어남)

    3. 그 외의 경우에는 이동하려는 방향으로 한 칸 이동.

        => 동전이 있는 곳이라도 갈 수 있음. 동전이 이동하고 나면, 그 곳은 빈 칸 '.'이 될테니깐

- 두 동전 중에서, 하나만 보드(MAP)에서 떨어뜨리기 위해 버튼을 최소 몇번을 눌러야하는지 구해라.



'''
# DFS 풀이1 (visited 배열 사용)


import sys, math
sys.setrecursionlimit(10**6)


N, M  = map(int, input().split())

MAP = [list(input().split()) for _ in range(N)]
visited = []
coins_position = []


# 이동의 방향을 위한 델타 배열
dr = [-1, 0, 1, 0]
dc = [0, -1,0, 1]

ans = math.inf

print(ans)


# coin1 : (row, col) // coin2 : (row, col) // cnt : 버튼을 누르는 횟수
def dfs(coin1, coin2, cnt):
    global ans

    row1, col1 = coin1
    row2, col2 = coin2

    # 가지치기 1 : 10번 보다 더 많이 눌러야 한다면 종료
    if cnt >= 10 :
        return

    # 가지치기 2 : cnt가 res보다 커지는 경우
    # why?! 우리는 최소의 cnt를 찾기 위해 ans를 갱신하고 있는 중
    if cnt >= ans:
        return 

    #가지치기 3: 두 동전 모두 MAP 밖으로 나가게 되는 경우
    if (0 > row1 or N <= row1 or 0 > col1 or M <= col1) and (0 > row2 or N <= row2 or 0 > col2 or M <= col2) :
        return
    
    
    # base 조건 : 두 동전 중에 하나만 MAP에서 떨어지게 되는 경우

    if (0 > row1 or N <= row1 or 0 > col1 or M <= col1) or (0 > row2 or N <= row2 or 0 > col2 or M <= col2) :
        ans = (cnt, ans)
        return
    
    # 재귀 연산 부분
    for i in range(4):
        next_row1 = row1 + dr[i]
        next_col1 = col1 + dc[i]
        next_row2 = row2 + dr[i]
        next_col2 = col2 + dc[i]

        # 이동 후 범위체크

        if 0 <= next_row1 < N and 0 <= next_col1 < M and 0 <= next_row2 < N and 0 <= next_col2 < M:
            pass


        else:
            pass