
#sol1


lst1 = [[1,2,3], [4,5,6]]
lst2 = [[7,8,9], [10, 11, 12]]

for nodes in [lst1, lst2] :
    print(nodes)


def solution(n, results):
    # wins[key] = key가 이긴 사람들의 집합
    # loses[key] = key가 이기지 못한 사람들의 집합
    wins, loses = {}, {}  #dict
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for battle in results:
            if battle[0] == i: # i의 승리. i가 이긴 사람들
                wins[i].add(battle[1])
            if battle[1] == i: # i의 패배. i가 진 사람들
                loses[i].add(battle[0])
        # i를 이긴 사람들 (loses[i]) =>  i를 이겼기 때문에, i에게 진 사람(wins[i])은 반드시 이긴다
        for winner in loses[i]:
            wins[winner].update(wins[i])

        # i에게 진 사람들 (wins[i]) => i에게도 졌기 때문에, i를 이긴 사람들(loses[i])에게는 반드시 진다
        for loser in wins[i]:
            loses[loser].update(loses[i])

    cnt = 0
    for i in range(1, n+1):
        # 나 자신을 제외하고(n - 1), 다른 사람들관의 서열정리가 다 된 경우
        if len(wins[i]) + len(loses[i]) == n - 1:
            cnt += 1
    return cnt


#sol2


from collections import deque


def solution(n, results):
    answer = 0

    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]

    #데이터 초기화
    for result in results:
        win[result[0]].append(result[1])
        lose[result[1]].append(result[0])

    # bfs
    # bfs를 통해서, 서열정리 한 것을 기록(visited)
    for i in range(1, n + 1):

        visited = [False for _ in range(n + 1)]
        visited[0] = visited[i] = True  # 0번은 사용 x, True로 사용 하지않게 처리

        for nodes in [win, lose]:  # win , lose 순서대로 nodes에 넣어서, win한번 보고, lose 한번 보고, 즉 nodes에 win, lose를 번갈아 교체함.

            q = deque([i])

            while q:
                idx = q.popleft()
                for node in nodes[idx]:
                    if not visited[node]:
                        visited[node] = True
                        q.append(node)

        # visted 배열을 봤는데, 각 개인간에 서열정리가 마무리된 상태.
        # 즉 False가 visited배열 안에 없다!
        if False not in visited:
            answer += 1

    return answer