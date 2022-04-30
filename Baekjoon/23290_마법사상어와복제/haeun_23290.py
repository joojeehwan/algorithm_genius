"""
아직 미완!!!!!
"""





# 물고기 개수 , 상어 연습 횟수
M, S = map(int, input().split())

# 물고기 이동 방향 델타. 방향 숫자 주어지는 그대로 쓰려고 9개로 만듦.
# 왼쪽, 왼쪽위, 위, 오른쪽위, 오른쪽, 오른쪽아래, 아래, 왼쪽아래
fish_dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
fish_dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 각 위치에 물고기의 방향'들'을 저장할 3차원 배열
fish = [[list()]*4 for _ in range(4)]

# 물고기 냄새 저장할 2차원 배열, 값은 0 or 1 or 2
fish_smell = [[0]*4 for _ in range(4)]

# 물고기
for _ in range(M):
    fish_r, fish_c, fish_d = map(int, input().split())
    # 위치만큼은 양보할 수 없다. 1씩 뺌
    fish[fish_r-1][fish_c-1] = [fish_d]

# 상어 이동 방향 델타. 물고기와 마찬가지로 그대로 쓰려고 5개로 만듦. 상1 좌2 하3 우4
shark_dr = [0, -1, 0, 1, 0]
shark_dc = [0, 0, -1, 0, 1]

# 상어
shark_row, shark_col = map(int, input().split())

# 물고기 이동
def move_fish(r, c, fish_directions):
    for fish_dir in fish_directions:
        found = False
        for i in range(8):
            # 45씩 반시계 회전
            new_fish_dir = (fish_dir - i) % 9
            if new_fish_dir == 0:
                new_fish_dir = 1
            next_r, next_c = r + fish_r[new_fish_dir], c + fish_c[new_fish_dir]
            if 0 > next_r or next_r > 4 or 0 > next_c or next_c > 4:
                continue
            if fish_smell[next_r][next_c]:
                continue
            if next_r == shark_row and next_c == shark_col:
                continue
            # 이동할 수 있다면
            fish[next_r][next_c].append(new_fish_dir)
            fish[]






# 상어 이동

# 냄새 제거

# 복제 마법 완료


# S번 동안 마법을 연습한다.
for turn in range(S):
    # 복제 마법 시전. 지금 배열들을 복사해둔다.
    copy_fish = [[[0]]* 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            copy_fish[r][c] = fish[r][c]

    # 모든 물고기가 한칸 이동한다.
    for r in range(4):
        for c in range(4):
            if fish[r][c]:
                move_fish(r, c, fish[r][c])
