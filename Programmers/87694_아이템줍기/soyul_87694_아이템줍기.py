def solution(rectangle, characterX, characterY, itemX, itemY):

    # 먼저 MAP에 테두리를 그려줌
    MAP = [[-1] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, x2 * 2 + 1):
            for j in range(y1 * 2, y2 * 2 + 1):
                if x1 * 2 < i < x2 * 2 and y1 * 2 < j < y2 * 2:  # 내부라면
                    MAP[i][j] = 0
                elif MAP[i][j] != 0:                    # 내부가 아니고 테두리라면
                    MAP[i][j] = 1

    # 최단 거리를 찾기 위한 bfs
    q = []
    q.append((characterX * 2, characterY * 2))
    visited = [[0] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = 1

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while q:
        now_i, now_j = q.pop(0)

        # 아이템을 먹었다면
        if now_i == itemX * 2 and now_j == itemY * 2:
            break

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어나거나 갈 수 없는 곳이거나 이미 갔던 곳이면
            if next_i < 0 or next_i >= 102 or next_j < 0 or next_j >= 102:
                continue
            if MAP[next_i][next_j] != 1:
                continue
            if visited[next_i][next_j]:
                continue

            q.append((next_i, next_j))
            visited[next_i][next_j] = visited[now_i][now_j] + 1

    answer = (visited[itemX * 2][itemY * 2] - 1) // 2
    return answer