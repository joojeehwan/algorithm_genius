"""
ㅠㅠ ㅋㅋㅋ 처음에 DFS로 풀려고 했다가 좌르르르륵 다 틀려서
질문 읽어보니 대부분 BFS로 풀더라고.. 그제서야
왜 나는 이걸 DFS로 풀려고 했지? 정말 멍청해졌구나 라는 생각이 들면서
BFS로 바꾸자마자 통과했음.
1108(+7) & 풀이시간 1시간 20분..ㅠㅠ
"""

from collections import deque


def solution(n, edge):
    answer = 0

    # 몇 번의 간선을 거쳐 왔는지 기록
    visited = [0] * (n + 1)
    visited[1] = 1
    # 연결 상태 기록
    connection = dict()

    for a, b in edge:
        if connection.get(a):
            connection[a] += [b]
        else:
            connection[a] = [b]
        if connection.get(b):
            connection[b] += [a]
        else:
            connection[b] = [a]

    queue = deque()
    queue.append(1)

    while queue:
        now = queue.popleft()
        connects = connection[now]

        for connect in connects:
            if not visited[connect]:
                visited[connect] = visited[now] + 1
                queue.append(connect)

    farthest = max(visited)

    for i in range(1, n + 1):
        if visited[i] == farthest:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))