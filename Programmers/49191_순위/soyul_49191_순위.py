from collections import deque

def solution(n, results):

    win = [[] for _ in range(n+1)]      # idx를 대상으로 이긴 번호를 idx에 넣음
    lose = [[] for _ in range(n+1)]     # idx를 대상으로 진 번호를 idx에 넣음

    for r in results:
        win[r[1]].append(r[0])          # [[], [], [4, 3, 1], [4], [], [2]]
        lose[r[0]].append(r[1])         # [[], [2], [5], [2], [3, 2], []]

    answer = 0

    for i in range(1, n+1):
        visited = [1] + [0] * (n)
        visited[i] = 1

        for nodes in [win, lose]:               # win 검사하고 lose 검사
            q = deque([i])
            while q:
                idx = q.popleft()
                for node in nodes[idx]:
                    if not visited[node]:
                        visited[node] = 1
                        q.append(node)

        if 0 not in visited:
            answer += 1

    return answer

"""
1부터 n+1까지 모두 확인
visited 배열에 내가 확인할 수 있는 것들을 표시해줌

ex) 내가 2번일 때,
3번이 나를 이기면 3을 이긴 사람들은 모두 나보다 순위가 높음
4가 나한테 지면 4한테 진 사람들은 모두 내가 이김

이긴 애들은 이기는 것들을 검사
진 애들은 진 애들을 검사
"""

"""
q = deque()
q.append(i)

while q:
    idx = q.popleft()
    for node in win[idx]:
        visited[node] = 1
        q.append(node)

q = deque()
q.append(i)

while q:
    idx = q.popleft()
    for node in lose[idx]:
        visited[node] = 1
        q.append(node)
        
이렇게 했더니 시간 초과 남
"""
