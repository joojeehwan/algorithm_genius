from  collections import deque


def fill_field(field, squares):
    max_r, max_c = 0, 0
    for square in squares:
        ldc, ldr, rtc, rtr = square
        max_r, max_c = max(max_r, rtr), max(max_c, rtc)
        # 기존 사이즈보다 두 배로 늘림 -> ㄷ자 테두리를 구분하기 위해
        for r in range(ldr * 2, rtr * 2 + 1):
            for c in range(ldc * 2, rtc * 2 + 1):
                if not field[r][c]:
                    field[r][c] = 1
    return max_r * 2 + 1, max_c * 2 + 1


def bordering(field, row, col):
    queue = deque()
    queue.append((0, 0))
    visited = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    visited[0][0] = 1
    while queue:
        now_r, now_c = queue.popleft()
        for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:  # 남동북서(8방향)
            new_r, new_c = now_r + dr, now_c + dc
            if new_r < 0 or new_r >= row + 1 or new_c < 0 or new_c >= col + 1:  # 맵 밖임
                continue
            if visited[new_r][new_c]:  # 이미 방문함
                continue
            visited[new_r][new_c] = 1
            if field[new_r][new_c] == 1:  # 테두리임
                field[new_r][new_c] = 2
            else:  # 빈 공간임
                queue.append((new_r, new_c))
    return

def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[0 for _ in range(102)] for _ in range(102)]
    # 맵 채우기
    row, col = fill_field(field, rectangle)

    # 테두리 구분하기 (BFS)
    bordering(field, row, col)

    # 테두리 따라 최단거리 계산하기 (BFS)
    queue = deque()
    queue.append((characterY * 2, characterX * 2))
    visited = [[row * col + 1 for _ in range(col + 1)] for _ in range(row + 1)]
    visited[characterY * 2][characterX * 2] = 0
    while queue:
        now_r, now_c = queue.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # 남동북서
            new_r, new_c = now_r + dr, now_c + dc
            if new_r < 0 or new_r >= row + 1 or new_c < 0 or new_c >= col + 1:  # 맵 밖임
                continue
            if (new_r, new_c) == (itemY * 2, itemX * 2):  # 도착함
                return (visited[now_r][now_c] + 1) // 2
            if field[new_r][new_c] < 2:  # 테두리가 아님
                continue
            if visited[new_r][new_c] < visited[now_r][now_c] + 1:  # 이미 방문함
                continue
            visited[new_r][new_c] = visited[now_r][now_c] + 1
            queue.append((new_r, new_c))



print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1,1,5,7]], 1, 1, 4, 7))
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))
print(solution([[2, 1, 3, 9], [1, 6, 10, 8], [7, 2, 9, 10], [4, 3, 11, 4]], 2, 2, 9, 5))
print(solution([[2, 1, 3, 9], [1, 6, 10, 8], [7, 2, 9, 10], [4, 3, 11, 4]], 3, 6, 9, 8))
print(solution([[2, 1, 3, 9], [1, 6, 10, 8], [7, 2, 9, 10], [4, 3, 11, 4]], 2, 8, 7, 3))
