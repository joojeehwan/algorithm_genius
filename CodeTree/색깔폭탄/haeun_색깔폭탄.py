"""
풀이 시간 : 1시간 49분
격자 놀이 총 집합
해설 보고 폭탄 중력 부분 개선
내 코드 :
- 색상, 빨강 visited 나눔으로써 이미 조회한 폭탄 묶음에 대해선 BFS 중복 방지
- 가장 큰 폭탄 묶음의 폭탄 위치를 pos에 저장함 => pos로 remove 진행
해설 :
- 모든 위치를 다 보면서 BFS 진행
- 위치 저장 X visited 바탕으로 지움 => remove때 BFS 진행

결과적으로는 해설이 더 빠르고, 메모리도 절약함
- pos 저장하고 하는 것 보다는 그냥 BFS를 도는게 나은 듯
"""

from collections import deque
from typing import List, Tuple

N, M = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(N))
answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

RED = M + 1  # 0을 빈칸으로 쓰기 위해서, 빨간색을 m 다음 숫자로 지정
block_visited = [[False] * N for _ in range(N)]  # 방문처리

# 가장 큰 폭탄 덩어리 찾기
# 1. 크기가 큰 폭탄 묶음 -> 빨간색 폭탄이 가장 적은 것
block_cnt, red_cnt = 0, 0
# 2. 기준점의 가장 행이 큰 -> 가장 열이 작은
max_row, min_col = 0, N + 1
# 해당 폭탄 묶음의 폭탄 위치들 저장
pos = []


def change_red() -> None:
    """
    빨간 폭탄을 m+1로 바꾸고, 빈칸은 0으로 사용한다.
    """
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                grid[r][c] = RED


def in_range(r: int, c: int) -> bool:
    """
    (r, c)가 격자 내에 있는지 확인한다.
    :param r: 행
    :param c: 열
    :return: 범위 내 True, 범위 밖 False
    """
    return 0 <= r < N and 0 <= c < N


def change_big_bomb(blocks: int, reds: int, row: int, col: int, positions: List[Tuple[int, int]]) -> None:
    """
    가장 큰 크기의 폭탄 묶음을 변경한다.
    :param blocks: 폭탄의 개수(빨강 제외)
    :param reds: 빨간 폭탄의 개수
    :param row: 기준점 행
    :param col: 기준점 열
    :param positions: 폭탄들의 위치
    :return:
    """
    # 전역 변수로 저장한 '가장 큰 크기의 폭탄 묶음 정보'
    global block_cnt, red_cnt, max_row, min_col, pos
    block_cnt = blocks
    red_cnt = reds
    max_row = row
    min_col = col

    pos.clear()
    for position in positions:
        pos.append(position)


def find_set(color: int, row: int, col: int) -> bool:
    """
    현재 격자에서 크기가 가장 큰 폭탄 묶음을 찾는다.
    :param color: 폭탄의 색(이것과 일치하거나 빨간색만 가능)
    :param row: 시작 행
    :param col: 시작 열
    :return: 폭탄 묶음의 조건(2개 이상, 빨간색만 X)을 만족 하는지
    """

    blocks, reds = 1, 0  # 하나 찾으면서 시작한거니깐 초기값은 1
    m_row, m_col = row, col
    now_pos = [(row, col)]

    visited = [[False] * N for _ in range(N)]
    visited[row][col] = True
    q = deque([(row, col)])

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 갈 수 없는 곳
            if not in_range(nr, nc) or visited[nr][nc]:
                continue
            # 빈칸
            if grid[nr][nc] == 0:
                continue
            # 내 색과 다른데 빨간색도 아님
            if grid[nr][nc] != color and grid[nr][nc] != RED:
                continue

            # 현재 BFS 방문 처리 + deque 추가 + 위치 기록
            visited[nr][nc] = True
            q.append((nr, nc))
            now_pos.append((nr, nc))

            # 각 색에 맞춰 개수 카운트
            if grid[nr][nc] == RED:
                reds += 1
            if grid[nr][nc] == color:
                # 기준점 계산
                if m_row < nr:
                    m_row, m_col = nr, nc
                elif m_row == nr and m_col > nc:
                    m_col = nc
                # 같은 묶음에 있는 같은 색의 폭탄은 또 BFS 안돌게끔
                block_visited[nr][nc] = True
                blocks += 1

    # 폭탄 묶음이란 2개 이상의 폭탄으로 이루어져 있어야 하며,
    # 모두 같은 색깔의 폭탄으로만 이루어져 있거나 빨간색 폭탄을 포함하여 정확히 2개의 색깔로만 이루어진 폭탄을 의미합니다.
    # 다만, 빨간색 폭탄으로만 이루어져 있는 경우는 올바른 폭탄 묶음이 아니며, 모든 폭탄들이 전부 격자 상에서 연결되어 있어야만 합니다.
    if blocks == 0 or blocks + reds < 2:
        return False

    # BFS 종료
    # 가장 큰 폭탄 묶음과 변경할 가치가 있는지 확인
    if blocks + reds > block_cnt + red_cnt:
        change_big_bomb(blocks, reds, m_row, m_col, now_pos)
    elif blocks + reds == block_cnt + red_cnt:
        if reds < red_cnt:
            change_big_bomb(blocks, reds, m_row, m_col, now_pos)
        elif reds == red_cnt:
            if m_row > max_row:
                change_big_bomb(blocks, reds, m_row, m_col, now_pos)
            elif m_row == max_row and m_col < min_col:
                change_big_bomb(blocks, reds, m_row, m_col, now_pos)

    return True


def find_largest_bomb() -> bool:
    """
    가장 큰 폭탄 묶음을 찾기 위해 한칸씩 돌아보면서, 폭탄 묶음이 하나라도 있는지 반환한다.
    :return: 폭탄 묶음이 하나라도 있으면 True, 없으면 False
    """
    global block_visited

    block_visited = [[False] * N for _ in range(N)]
    found = False

    for r in range(N):
        for c in range(N):
            # 빈칸, 빨간색, 검은 돌, 이미 방문 => PASS
            if grid[r][c] == 0 or grid[r][c] == RED or grid[r][c] == -1 or block_visited[r][c]:
                continue
            block_visited[r][c] = True
            # 해당 위치에서 폭탄 묶음이 만들어 지는지 확인
            if find_set(grid[r][c], r, c):
                found = True

    return found


def remove_bomb() -> None:
    """
    선택된 폭탄 묶음에 해당되는 폭탄들을 전부 제거합니다.
    :return:
    """
    global answer
    # 가장 큰 폭탄 묶음의 폭탄 위치들을 pos에 저장해왔다.
    answer += len(pos) ** 2
    for r, c in pos:
        grid[r][c] = 0


def gravity() -> None:
    """
    폭탄들이 제거된 이후에는 중력이 작용하여 위에 있던 폭탄들이 떨어짐
    :return:
    """
    moved = [[0] * N for _ in range(N)]

    # 열 -> 행 순으로 돌면서
    for c in range(N):
        # 마지막으로 쌓인 위치를 기록한다.
        last_idx = N-1
        for r in range(N - 1, -1, -1):
            # 돌은 특이한 성질을 띄고 있기 때문에 중력이 작용하더라도 떨어지지 않습니다.
            if grid[r][c] == -1:
                last_idx = r
            if grid[r][c] == 0:
                continue
            moved[last_idx][c] = grid[r][c]
            last_idx -= 1

    # 다시 복사
    for r in range(N):
        grid[r] = moved[r][:]


def rotate_reverse_clock() -> None:
    """
    반시계 방향으로 90' 회전 공식 = [N-c-1][r] = [r][c]
    :return:
    """
    new_grid = [[0] * N for _ in range(N)]

    # 회전
    for r in range(N):
        for c in range(N):
            new_grid[N - c - 1][r] = grid[r][c]

    # 복사붙여넣기
    for r in range(N):
        grid[r] = new_grid[r][:]


def solution() -> None:
    """
    각 단계 수행
    :return:
    """
    global block_cnt, red_cnt, max_row, min_col, pos
    change_red()

    while find_largest_bomb():

        remove_bomb()

        gravity()

        rotate_reverse_clock()

        gravity()
        # 초기화
        block_cnt, red_cnt, max_row, min_col = 0, 0, 0, N + 1
        pos.clear()

    print(answer)


solution()