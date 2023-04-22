# bfs문제 유형 정리





1. ## 최단거리 값 구하기



2. ## 값은 값 그룹의 갯수  혹은 그들의 값 계산 구하기 



````python
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs(row, col, visited, maps, N, M) :

    cnt = int(maps[row][col])
    q = deque()
    q.append((row, col))
    visited[row][col] = True

    while q:

        now_row, now_col = q.popleft()

        for i in range(4):

            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if 0 <= next_row < M and 0 <= next_col < N :

                if maps[next_row][next_col] != 'X' and not visited[next_row][next_col]:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
                    cnt += int(maps[next_row][next_col])

    return cnt

def solution(maps):

    answer = []
    N = len(maps[0])
    M = len(maps)
    visited = [[False] * N for _ in range(M)]

    for row in range(M) :
        for col in range(N) :
            if maps[row][col] != 'X' and not visited[row][col]:
                temp = bfs(row, col, visited, maps, N, M)
                answer.append(temp)

    answer.sort()

    if answer == []:
        return [-1]
    return answer
````





3. ## 최단거리 경로



4. ## 가중치 배열 만들어 최단거리 고려(다익스트라)



```python
import math
from collections import deque


def solution(board):
    def bfs(start):
    
        # table[y][x] = 해당 위치에 도달하는 최솟값
        table = [[math.inf for _ in range(len(board))] for _ in range(len(board))]

        #진행 방향 위 0 , 왼쪽 1 , 아래 2, 오른쪽 3
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = deque([start])
        #초기 비용은 0
        table[0][0] = 0
        while q:
            #row, col , 비용, 진행방향
            row, col, cost, head = q.popleft()
            for idx , (dr, dc) in enumerate(dirs):
                next_row = row + dr
                next_col = col + dc

                #진행방향과 다음 방향이 일치하면 + 100, 다르면 전환비용 500 + 진행비용 100 = 600

                next_cost = cost + 600 if idx != head else cost + 100

                if 0 <= next_row < len(board) and 0 <= next_col < len(board) and board[next_row][next_col] == 0 and table[next_row][next_col] > next_cost:
                    table[next_row][next_col] = next_cost
                    q.append((next_row, next_col, next_cost, idx))

        return table[-1][-1]
    return min(bfs((0,0,0,2)), bfs((0,0,0,3)))
```

