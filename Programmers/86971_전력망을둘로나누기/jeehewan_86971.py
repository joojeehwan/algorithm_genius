

'''


전력망을 두개 나누기 위해서,

잘라는 부분에서 고민을 함,,

remove함수를 사용

그외에는 bfs를 사용해서, 전령망의 갯수를 counting


union - find로도 푸네,, 흠흠


'''


#bfs
from collections import deque


def bfs(start, n, graph):
    cnt = 0

    q = deque()
    q.append(start)

    visited = [False for _ in range(n + 1)]
    visited[start] = True

    while q:

        node = q.popleft()

        for i in graph[node]:

            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1

    return cnt


def solution(n, wires):
    answer = 101

    graph = [[] for _ in range(n + 1)]

    for n1, n2 in wires:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # cutting
    for i in range(n - 1):
        graph[wires[i][0]].remove(wires[i][1])
        graph[wires[i][1]].remove(wires[i][0])

        # check node cnt

        cntNode1 = bfs(wires[i][0], n, graph)
        cntNode2 = bfs(wires[i][1], n, graph)

        answer = min(answer, abs(cntNode1 - cntNode2))

        # re conneect for next check
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

    return answer


#dfs - stack

def dfs(start, n ,graph):
    visited = [False for _ in range(n + 1)]
    stack = [start]
    visited[start] = True

    res = 0
    while stack:

        node = stack.pop()
        res += 1

        for v in graph[node]:
            if v not in stack and not visited[v]:
                visited[v] = True
                stack.append(v)

    return res

def solution(n, wires):
    answer = 101

    for k in range(n - 1):

        temp = wires[:]
        a, b = temp.pop(k)

        graph = [[] for _ in range(n + 1)]

        for x, y in temp:
            graph[x].append(y)
            graph[y].append(x)

        answer = min(answer, abs(dfs(a, n, graph) - dfs(b, n ,graph)))

    return answer


#dfs - 재귀

def dfs(start, visited, graph):
    global cnt
    visited[start] = True

    cnt += 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i, visited, graph)


def solution(n, wires):
    global cnt
    graph = [[] for _ in range(n + 1)]

    answer = 102

    for n1, n2 in wires:
        graph[n1].append(n2)
        graph[n2].append(n1)

    for n1, n2 in wires:
        graph[n1].remove(n2)
        graph[n2].remove(n1)

        cnt = 0
        visited = [False for _ in range(n + 1)]
        dfs(1, visited, graph)

        answer = min(answer, abs(n - 2 * cnt))

        graph[n1].append(n2)
        graph[n2].append(n1)

    return answer


