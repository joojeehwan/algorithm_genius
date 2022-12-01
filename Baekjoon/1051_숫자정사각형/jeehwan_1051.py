'''

완전 탐색


전체 격자에서,
'''


import sys


n, m = map(int, sys.stdin.readline().split())
MAP = [list(map(int ,sys.stdin.readline().strip())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(m):
        target = MAP[i][j] # 현재 꼭짓점에 쓰여 있는 수
        # 반복문을 통해 j축에 target과 똑같은 수를 확인
        for k in range(j, m):
            # target과 똑같은 수가 있다면 정사각형 위치가 범위 내에 있고 똑같은 수가 있는지 확인
            # i + k - j : 세로 길이(row 좌표) / k : 가로 길이(col 좌표)
            # target(MAP[i][j])과 같은 MAP[i][K]를 찾고, 이제 아래의 두 꼭지점이 같은 것을 찾는 로직
            # 쉽게 생각해, 격자 위에 사각형의 꼭짓점을 좌표로 찾아간다 생각
            # 완전 탐색으로 모든 MAP[i][j]를 돌면서, 확인
            if MAP[i][k] == target and i + k - j < n and k < m:
                #좌측 하단 MAP[i + k - j][j] // 우측 하단 MAP[i + k - j][k]
                if MAP[i + k - j][j] == target and MAP[i + k - j][k] == target:

                    # 정사각형 위치에 모두 똑같은 수가 있다면 길이를 제곱
                    answer.append((k - j + 1) ** 2)

# 제일 큰 정사각형의 크기를 출력
print(max(answer))