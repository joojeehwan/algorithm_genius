
#메모리 초과
#dfs 풀이
import sys
sys.setrecursionlimit(20000)

#그룹에 포함하고 안하고를 1 과 -1 로 구분한다
def dfs(now, group):

    global flag

    if flag:
        return

    #그룹 등록
    visited[now] = group

    for next in MAP[now]: #내가 갈 수 있는 다음 노드들 중에서!
        if not visited[next]: #안가본 곳이면!
            dfs(next, -group) #나와는 다른 그룹에 넣는다!
        elif visited[now] == visited[next]: #인접한데 같은 그룹이라면!
            flag = True
            return #그 후에 종료!

T = int(input())


for _ in range(T):

    #정점과 간선의 갯수 입력받기
    V, E = map(int, input().split())
    #빈 그래프 만들기 => 1번 노드에서 부터 시작하니깐!
    MAP = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1) #방문한 정점 체크
    flag = False

    #데이터 전처리 => 무방향 그래프
    for _ in range(E):
        frm, to = map(int, input().split())
        MAP[frm].append(to)
        MAP[to].append(frm)

    # print(MAP)

    for i in range(1, V + 1):
        if not visited[i]: #방문 x
            dfs(i, 1) #dfs 돌아본다!각각의 점마다!
            if flag:
                break
    if flag:
        print("NO")
    else:
        print("YES")


from collections import deque


def bfs(start, group):

    q = deque()
    q.append((start))
    visited[start] = group

    while q:

        now = q.popleft()

        for next in MAP[now]: #해당 정점에서 갈 수 있는 곳!
            if not visited[next] : #그러나 가보지 못한 곳으로
                q.append((next))
                #1이면 -1이 담기고, -1이면 1이 담기도록 하기 위해서 -1을 곱해서!
                visited[next] = -1 * visited[now] #now에 있는 정점과 다른 정점으로!
            elif visited[next] == visited[now]: #인접한데 같은 그룹이라면
                return False
    return True


T = int(input())

for _ in range(T):

    #정점과 간선의 갯수 입력받기
    V, E = map(int, input().split())
    #빈 그래프 만들기 => 1번 노드에서 부터 시작하니깐!
    MAP = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1) #방문한 정점 체크

    #데이터 전처리 => 무방향 그래프
    for _ in range(E):
        frm, to = map(int, input().split())
        MAP[frm].append(to)
        MAP[to].append(frm)

    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')
