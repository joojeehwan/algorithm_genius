from collections import deque
import sys


def biggest_block(field, size):

    maxi_blocks = [[], []]  # 최대 크기 그룹 리스트
    for row in range(size):
        for col in range(size):
            visited = [[0] * size for _ in range(size)]
            if field[row][col] > 0:
                queue = deque()
                queue.append((row, col))
                visited[row][col] = 1
                block_lst = [[], []]  # 이 그룹의 블록 리스트
                key = field[row][col]  # 이 그룹의 블록 색
                while queue:
                    now_r, now_c = queue.popleft()
                    if not field[now_r][now_c]:  # 무지개 블록
                        block_lst[0].append((now_r, now_c))
                    else:  # 색 블록
                        block_lst[1].append((now_r, now_c))
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        # 새로운 좌표
                        new_r, new_c = now_r + dr, now_c + dc
                        # 걸러짐
                        if new_r < 0 or new_r >= size or new_c < 0 or new_c >= size:  # 맵 밖임
                            continue
                        if visited[new_r][new_c]:  # 이미 방문함
                            continue
                        if field[new_r][new_c] <= -1:  # 검은색 블록 or 빈 칸
                            continue
                        if field[new_r][new_c] > 0 and field[new_r][new_c] != key:  # 같은 색 블록이 아님
                            continue
                        # 방문
                        queue.append((new_r, new_c))
                        visited[new_r][new_c] = 1
                # 가장 큰 그룹이 될 조건
                if not block_lst[1]:  # 일반 블록이 없음
                    continue
                if len(block_lst[0]) + len(block_lst[1]) < 2:  # 블록이 두 개 이상
                    continue
                if len(maxi_blocks[0]) + len(maxi_blocks[1]) < len(block_lst[0]) + len(block_lst[1]):
                    maxi_blocks = block_lst[:]
                elif len(maxi_blocks[0]) + len(maxi_blocks[1]) == len(block_lst[0]) + len(block_lst[1]):  # 블록 수가 같을 경우
                    if len(maxi_blocks[0]) < len(block_lst[0]):  # 무지개 블록이 많으면 갱신
                        maxi_blocks = block_lst[:]
                    elif len(maxi_blocks[0]) == len(block_lst[0]):  # 무지개 블록도 같으면
                        if sorted(maxi_blocks[1])[0] < sorted(block_lst[1])[0]:  # 기준 블록이 가장 뒤에 있는 그룹
                            maxi_blocks = block_lst[:]

    return maxi_blocks[0] + maxi_blocks[1]


def gravity(field, size):
    new_field = [[-2] * size for _ in range(size)]
    for row in range(size - 1, -1, -1):
        for col in range(size):
            if row == size - 1:  # 맨 밑
                new_field[row][col] = field[row][col]
            else:
                i = 0
                if field[row][col] >= 0 and new_field[row + i + 1][col] == -2:  # 무지개 or 일반 블록
                    while row + i + 1 < size and new_field[row + i + 1][col] == -2:
                        i += 1
                    new_field[row + i][col] = field[row][col]
                else:
                    new_field[row][col] = field[row][col]
    return new_field


def turn(field, size):
    new_field = [[-2] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            new_field[size - 1 - col][row] = field[row][col]
    return new_field


size, colors = map(int, sys.stdin.readline().split())  # 격자 크기, 색상 수
field = [[] for _ in range(size)]  # 격자 상태
for r in range(size):
    field[r] = list(map(int, sys.stdin.readline().split()))
score = 0
# print('----- 격자 상태 -----')
# for f in field:
#     print(f)
# print()

# 1. 크기가 가장 큰 블록 그룹 찾기 (BFS)
biggest_group = biggest_block(field, size)
# print('----- 크기가 가장 큰 블록 그룹 -----')
# print(biggest_group)
# print()

while biggest_group:
    # 2. 가장 큰 블록 그룹 제거
    for br, bc in biggest_group:
        field[br][bc] = -2  # 빈 칸(-2)
    score += len(biggest_group) ** 2
    # print('----- 블록 그룹 제거 -----')
    # print('점수: ', score)
    # for f in field:
    #     print(f)
    # print()

    # 3. 중력
    field = gravity(field, size)
    # print('----- 중력 후 -----')
    # for f in field:
    #     print(f)
    # print()

    # 4. 90도 반시계 회전
    field = turn(field, size)
    # print('----- 회전 후 -----')
    # for f in field:
    #     print(f)
    # print()

    # 5. 중력
    field = gravity(field, size)
    # print('----- 중력 후 -----')
    # for f in field:
    #     print(f)
    # print()

    # 1. 크기가 가장 큰 블록 그룹 찾기 (BFS)
    biggest_group = biggest_block(field, size)
    # print('----- 크기가 가장 큰 블록 그룹 -----')
    # print(biggest_group)
    # print()

print(score)