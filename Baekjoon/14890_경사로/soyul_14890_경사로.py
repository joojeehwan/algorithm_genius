import sys

N, L = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 검사하는 함수
# 높이가 높아지거나 낮아질 때 지나온 길이가 경사로 길이 이상이어야 함
def check(i, k):
    # 가로 검사
    if k == 1:
        dis = 1                                 # 경사로를 놓을 만큼의 길이 있는지 기록하는 변수
        j = 1
        while j < N:
            if MAP[i][j-1] == MAP[i][j]:        # 높이가 옆이랑 같으면
                dis += 1
            elif MAP[i][j] - MAP[i][j-1] == 1:      # 높이가 1만큼 높아졌다면
                if dis < L:                         # 경사로를 놓을 만큼 길이가 안된다면 끝
                    return 0
                else:
                    dis = 1
            elif MAP[i][j] - MAP[i][j-1] == -1:     # 높이가 1만큼 낮아졌다면 경사로를 놓을 공간이 있는지 검사
                dis = 1
                j += 1
                while dis < L and j < N:
                    if MAP[i][j-1] != MAP[i][j]:          # 만약 안되면 바로 끝
                        return 0
                    j += 1
                    dis += 1
                if dis < L:
                    return 0
                dis = 0
                j -= 1
            else:
                return 0
            j += 1
        return 1
    # 세로 검사
    else:
        dis = 1
        j = 1
        while j < N:
            if MAP[j-1][i] == MAP[j][i]:        # 높이가 옆이랑 같으면
                dis += 1
            elif MAP[j][i] - MAP[j-1][i] == 1:      # 높이가 1만큼 높아졌다면
                if dis < L:                         # 경사로를 놓을 만큼 길이가 안된다면 끝
                    return 0
                else:
                    dis = 1
            elif MAP[j][i] - MAP[j-1][i] == -1:     # 높이가 1만큼 낮아졌다면 경사로를 놓을 공간이 있는지 검사
                dis = 1
                j += 1
                while dis < L and j < N:
                    if MAP[j-1][i] != MAP[j][i]:          # 만약 안되면 바로 끝
                        return 0
                    j += 1
                    dis += 1
                if dis < L:
                    return 0
                dis = 0
                j -= 1
            else:
                return 0
            j += 1
        return 1

ans = 0

for i in range(N):
    ans += check(i, 1)
    ans += check(i, 0)

print(ans)