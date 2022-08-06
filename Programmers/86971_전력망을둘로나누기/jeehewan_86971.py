


#bfs 풀이

'''


전력망을 두개 나누기 위해서,

잘라는 부분에서 고민을 함,,

remove함수를 사용

그외에는 bfs를 사용해서, 전령망의 갯수를 counting

dfs 풀이도 할 예정


'''


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