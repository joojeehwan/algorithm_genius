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



````py
#여기가 문제의 그 부분,,,!
def tryRaser(attacker, target):

    visited = [[False for _ in range(M)]for _ in range(N)]

    backTracking = [[None for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append(attacker)
    visited[attacker[0]][attacker[1]] = True

    while q :
        now_row, now_col = q.popleft()

        for k in range(4) :

            #모듈려 연산
            next_row = (now_row + dr[k] + N) % N
            next_col = (now_col + dc[k] + M ) % M

            # 범위 생각?! 여기선 할 필요 없다..!
            # 범위 밖이라는 것이 존재하지 않아

            # 이미 간곳도 가지 않아.
            if visited[next_row][next_col] :
                continue

            # 부서진 포탑이 있는 곳은 갈 수 없다.
            if MAP[next_row][next_col] == 0:
                continue

            #(next_row, next_col)은 (now_row, now_col)에서 왔다.
            backTracking[next_row][next_col] = (now_row, now_col)
            visited[next_row][next_col] = True
            q.append((next_row, next_col))

    # 결국 타켓까지 가지 못하는 경우
    # 이어져 있는 포탑의 경로가 없는 경우
    if not visited[target[0]][target[1]]:
        return False


    # 레이저가 도달할 수 있는 경우?!
    # 백 트래킹 돌면서, 가는 경로에 있는 포탑들의 공격력 낮추기
    row, col = target

    while row != attacker[0] or col != attacker[1] :
        power = MAP[attacker[0]][attacker[1]] // 2

        #공격이 대상은 //2 안하고 공격
        if row == target[0] and col == target[1] :
            power = MAP[attacker[0]][attacker[1]]

        MAP[row][col] = attack(row, col, power)
        # 아래 코드를 통해서, 현재의 row, col에 오기 위해 왔던
        # 이전 (row, col)를 찾아갈 수 있음.
        row, col = backTracking[row][col]
````







````python
# node case
from collections import deque

def bfs(graph, start, end) : 

    visited = [False]  * len(graph)
    q = deque()
    q.append(start)
    visited[start] = True
    #이전 노드를 기록하는 배열
    prev = [-1] * len(graph)

    while q : 
        now_node = q.popleft()
        debug = 1
        for next_node in graph[now_node] : 
            if not visited[next_node]:
                q.append(next_node)
                # 다음 번 갈 노드와 현재 내가 있는 노드를 알 수 있으니, 
                # "다음 번 갈 노드(next_node)의 이전은 무엇?! 그건 바로 지금(now_node)" 
                # prev라는 배열안에는, start 부터 end까지 가면서, 어떤 노드를 통해 이동했는지 기록
                # ex) [-1, 0, 0, 1, 1, 2, 2]
                # 라고 적혀있다면, start 0번 노드 , end 6번노드 이므로, 
                # 6번 노드에 최단거리로 도착하기 위해 2번노드 방문 => prev[6] = 2
                # 2번 노드에 최단거리로 도착하기 위해 0번노드 반문 => prev[2] = 0
                # 0번 노드는 시작 노드
                visited[next_node] = True
                prev[next_node] = now_node

                if next_node == end:
                    return prev

    return None

def find_path(prev, start, end) : 

    path  = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = prev[curr]

    path.append(start)
    path.reverse()
    return path
    
#인접행렬 정리
MAP = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1], [2], [2]]

start = 0

end = 6

prev = bfs(MAP, 0, 6)

if prev is None : 
    print("연결된 경로가 없음")

else:
    path = find_path(prev, start, end)
    print("가장 짧은 경로", path)
````





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

