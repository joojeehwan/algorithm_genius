from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):

    field = [[0] * 101 for _ in range(101)]
    # 크기만큼 다 1로 채우기
    for ldx, ldy, rux, ruy in rectangle:
        for row in range(ldx*2, rux * 2 + 1):
            for col in range(ldy*2, ruy * 2 + 1):
                field[row][col] = 1

    # 내부를 다시 0으로 바꾸기
    for ldx, ldy, rux, ruy in rectangle:
        for row in range(ldx*2 + 1, rux * 2):
            for col in range(ldy*2 + 1, ruy * 2):
                field[row][col] = 0

    # 탐험하기
    visited = [[0] * 101 for _ in range(101)]
    visited[characterX*2][characterY*2] = 1
    queue = deque([(characterX*2, characterY*2)])

    while queue:
        now_row, now_col = queue.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = now_row + dr, now_col + dc
            if 0 < next_row < 101 and 0 < next_col < 101:
                if not visited[next_row][next_col] and field[next_row][next_col]:
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    queue.append((next_row, next_col))
                if next_row == itemX*2 and next_col == itemY*2:
                    return (visited[next_row][next_col]-1) // 2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))