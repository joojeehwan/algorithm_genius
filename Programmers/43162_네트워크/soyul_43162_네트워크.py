def solution(n, computers):

    visited = [0] * n
    answer = 0

    # 처음컴퓨터부터 마지막컴퓨터까지 검사
    for i in range(n):
        if visited[i]:      # 이미 체크한 컴퓨터면 패스
            continue

        visited[i] = 1              # 새로운 네트워크 카운트 시작
        answer += 1
        q = []
        q.append(i)

        while q:                    # bfs로 연결된 네트워크 검사
            now = q.pop(0)

            for j in range(n):
                if visited[j]:          # 이미 체크한 컴퓨터면 패스
                    continue

                if computers[now][j]:            # 연결되어있다면
                    visited[j] = 1
                    q.append(j)
    return answer