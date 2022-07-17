from collections import deque
import sys


# 연합 정보 갱신
def make_union():
    flag = 0  # 인구 이동이 일어났는지
    union_lst = [[0] * size for _ in range(size)]  # 연합 정보
    # 델타 이동 (북, 서, 남, 동)
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    for r in range(size):
        for c in range(size):
            if union_lst[r][c]:  # 이미 연합임
                continue
            queue = deque()
            queue.append((r, c))  # (row, col)을 기준으로 연합인지 확인
            this_union = set()  # 이번 팀(team_num)의 연합 리스트
            u_people = 0  # 이 연합 인구 수
            while queue:  # BFS
                now_r, now_c = queue.popleft()
                for d in range(4):
                    # 한 칸 이동
                    new_r = now_r + dr[d]
                    new_c = now_c + dc[d]
                    if 0 <= new_r < size and 0 <= new_c < size:  # 지도 범위 안일때만
                        if not union_lst[new_r][new_c]:  # 연합이 아닐때만
                            if less <= abs(people[now_r][now_c] - people[new_r][new_c]) <= more:  # 두 나라의 차이가 범위 안일때만
                                queue.append((new_r, new_c))
                                # 연합 가입
                                union_lst[new_r][new_c] = 1
                                this_union.add((new_r, new_c))
                                u_people += people[new_r][new_c]
            # 연합 인구수, 연합 수 세기
            if len(this_union):  # 연합이 있다면
                after_people = u_people // len(this_union)  # 이동한 후의 인구
                # 인구 이동
                for u_r, u_c in this_union:
                    people[u_r][u_c] = after_people
                flag = 1
    return flag


size, less, more = map(int, sys.stdin.readline().split())  # 땅 크기, 인구 차이 범위 (less 이상 more이하)
people = [[] for _ in range(size)]  # 인구수 정보
for _ in range(size):
    people[_] = list(map(int, sys.stdin.readline().split()))
day = 0  # 인구 이동 날짜 수


while True:
    flag = make_union()  # 연합 정보 갱신
    if flag:
        day += 1
    else:
        print(day)
        break
