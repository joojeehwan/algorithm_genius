from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        # 아직 간 곳이 아니라면
        if not visited[i]:
            # 네트워크 개수 늘리고
            answer += 1
            queue = deque()
            queue.append(i)
            visited[i] = 1
            # 네트워크 찾기
            while queue:
                now = queue.popleft()
                for j in range(n): # 여기서 now부터 시작했다가 틀림, 이전 번호의 네트워크와 연결되어있을 수도 있다.
                    # 본인과 같으면 볼 필요 없고, 연결 안되어있으면 볼 필요 없고, 이미 방문했다면 볼 필요 없다.
                    # 여기서 조건 제대로 설정 안해줘서 또 틀림 ㅎ
                    if now != j and computers[now][j] and not visited[j]:
                        queue.append(j)
                        visited[j] = 1

    return answer

# print(solution(5,
#                [
#                    [1, 1, 1, 0, 0],
#                    [1, 1, 0, 0, 1],
#                    [1, 0, 1, 0, 0],
#                    [0, 0, 0, 1, 1],
#                    [0, 1, 0, 1, 1]
#                ]))
