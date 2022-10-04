import sys

N, L = map(int, sys.stdin.readline().split())
grid = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

answer = 0

# 열을 행으로 만들어서 추가해야한다.
for col in range(N):
    new_line = []
    for row in range(N):
        new_line.append(grid[row][col])
    grid.append(new_line)

# 2N개의 경사로를 다 검사한다.
for line in grid:
    # 경사로 끝나기 전까지 해결 되는지 확인한다.
    idx = 0
    continuous = 1
    possible = True
    while idx < N-1:
        if line[idx] == line[idx+1]:
            continuous += 1
            idx += 1
            continue
        # 높이차가 1 이상이면 경사로 불가
        if abs(line[idx] - line[idx+1]) > 1:
            possible = False
            break
        # 높이가 낮아지는 경우
        if line[idx] - 1 == line[idx+1]:
            # 남은 길이로 경사로를 만들 수 없는 경우
            if N - idx - 1 < L:
                possible = False
                break
            # 경사로를 만들 거리는 있는데
            for j in range(1, L+1):
                # 높이가 일정하지 않은 경우
                if line[idx] != line[idx+j]:
                    possible = False
                    break
            # 높이가 일정했다면 넘어가자!
            if possible:
                continuous = 0
                idx += L
        # 높이가 높아지는 경우
        elif line[idx] + 1 == line[idx+1]:
            if continuous < L:
                possible = False
                break
            elif continuous == L:
                continuous = 0
                idx += 1
        if not possible:
            break
    # 한 줄 끝까지 갔으면 하나 추가
    if possible:
        print(line)
        answer += 1

print(answer)