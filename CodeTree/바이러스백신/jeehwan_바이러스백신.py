'''

해당 문제를 풀 수 있는 2가지 sol


1. 각각의 바이러스에 대해 bfs를 통해 해당 바이러스로 부터 가장 멀리 떨어져 있는
병원까지의 거리를 구하고, 이 거리들 중 최대 거리가 결국 선택된 병원들로 부터
가장 멀리 떨어진 바이러스까지의 거리를 의미
=> 가능한 모든 조합에 대해 최대 거리를 꼐산하여 그 중 최솟값을 구하면 답이 된다.



2. 선택된 m개의 병원을 시작점으로 하여 bfs를 한번에 돌리기

가중치가 동일한 그래프에서 시작점이 여러 개인 상태로 bfs를 돌리게 되면, 그 각각의 시작점으로부터 거리가 가장 가까운 정점부터 큐에서 나오게 되기 때문에
문제에서 원하는 조건인, 바이러스 중 가장 가까운 병원까지의 거리가 가까운 바이러스 부터 선택되어 최단거리를 올바로 구할 수 있게 됨.



바이러스 : 0

벽 : 1

병원 : 2

지환 참고

# 조합 ver2

lst = [1, 2, 3, 4, 5]

target = 2

n = len(lst)

answer = []


def dfs_2(lev, cnt, temp):

    # 전체를 다 돌고
    if lev == n:

        # 해당 경우의 수의 요소의 갯수가, 내가 찾고자 하는 경우의 수 갯수와 같다면
        if cnt == target:
            answer.append(temp[:])

        return

    temp.append(lst[lev])
    dfs_2(lev + 1, cnt + 1, temp)
    temp.pop()
    dfs_2(lev + 1, cnt, temp)


dfs_2(0, 0, [])
print(answer)
'''


from collections import deque
import sys
sys.setrecursionlimit(9999)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

INF = 1e9

n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

#전체 병원 중에서 m개의 가짓수를 뽑는 경우의 수 확인
hospital_comb = []


answer = INF


# 전체 병원을 선택하는 경우의 수 판단
def dfs(hospital_lst, candidate_lst, lev) :

    #전체를 다 돌고,
    if lev == len(hospital_lst):
        # 해당 경우의 수의 요소가, 내가 찾고자 하는 경우의 수 갯수와 같다면
        if len(candidate_lst) == m :
            hospital_comb.append(candidate_lst[:])
        return

    # lev은 자체는 증가 되는 것이 맞음. 
    # 이 dfs에서는 candidate_lst 자체에 값을 넣고 뺴면서, 값을 변화시키는 것. (원본의 cnt + 1 , cnt 부분)
    candidate_lst.append(hospital_lst[lev])
    dfs(hospital_lst, candidate_lst, lev + 1)
    candidate_lst.pop()
    dfs(hospital_lst, candidate_lst, lev + 1)

def bfs(hospital_lst) :

    global answer

    q = deque()
    visited = [[False] * n for _ in range(n)]
    time_maps = [[0] * n for _ in range(n)]

    # 초기에 선택된 병원들의 값들을 q에다가 넣어두고, visited 배열 체크
    # 지금 visited 배열이 False, True의 형태 이므로, 최단 거리를 구하기 위해서, cnt라는 변수와 해당 cnt를 기록할 수 있는 2차원 배열(time_maps)을 만들어
    # 최단거리를 기록
    for hos in hospital_lst :
        q.append((hos[0],hos[1], 0))
        visited[hos[0]][hos[1]] = True

    while q :

        now_row, now_col , cnt = q.popleft()

        for i in range(4) :
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            #범위 체크 // 한번도 가지 않은 곳
            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col] :
                if MAP[next_row][next_col] == 0 or MAP[next_row][next_col] == 2:
                    q.append((next_row, next_col, cnt + 1))
                    visited[next_row][next_col] = True
                    time_maps[next_row][next_col] =  cnt + 1

    time = 0
    for row in range(n):
        for col in range(n):
            #이 경우는 모든 바이러스를 없애진 못한 경우, time_maps가 변하지 않고 그대로인 경우
            if MAP[row][col] == 0 and time_maps[row][col] == 0 :
                return

            if MAP[row][col] == 0:
                #각 케이스별 모든 바이러스를 없애는 데 걸리는 시간 
                time = max(time, time_maps[row][col])
    # 그 시간들 중 가장 잛은, 최단 시간을 구해 정답으로 출력
    answer = min(answer, time)

hospital = []
for row in range(n):
    for col in range(n):

        if MAP[row][col] == 2:
            hospital.append((row, col))

dfs(hospital, [], 0)

for i in range(len(hospital_comb)) :
    bfs(hospital_comb[i])

print(-1) if answer == INF else print(answer)



