def solution(n, wires):

    answer = n

    # 한 그룹에 네트워크가 몇 개 있는지 검사(1과 연결된그룹 하나만 검사 어차피 두그룹밖에 없으니까)
    def bfs():
        visited = [0] * (n + 1)
        q = []
        visited[1] = 1
        q.append(1)
        cnt = 1

        while q:
            now = q.pop(0)

            for next in tree[now]:
                if visited[next]:
                    continue

                visited[next] = 1
                q.append(next)
                cnt += 1

        return cnt

    # 전선을 순서대로 하나씩 끊어서 네트워크를 구성하는 트리를 만든다
    for i in range(len(wires)):
        tree = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j:
                continue
            w1, w2 = wires[j]
            tree[w1].append(w2)
            tree[w2].append(w1)
        nextwork_1 = bfs()
        nextwork_2 = n - nextwork_1

        answer = min(answer, abs(nextwork_1 - nextwork_2))

        if answer == 0:                                     # 차이가 없으면 그게 최소니까 바로 반환
            return answer

    return answer
