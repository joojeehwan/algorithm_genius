# import sys
# sys.stdin = open('input.txt', 'r')
"""
정신이 혼미
combinations와 deque를 써도 되는지 걱정스러워 테스트 돌려보니까 되길래 썼다.
쓰면서 점점 스파게티 코드가 되어가는걸 느꼈다
변수명이 너무 많아서 스스로 헷갈린다.
궁금한건 위에 반복문에서 쓴 index 명은 다시 재탕하는건 안좋은 버릇인건지...
다시 초기화해서 쓸 수는 있는데 어찌되었든 찌거기는 남아있으니까...
너무 힘들다
푼 시간 : 2시간 36분
메모리 : 68,628kb
실행시간 : 445ms
"""
from itertools import combinations
from collections import deque

T = int(input())

for tc in range(T):
    answer = 987654321
    N = int(input())
    room = list(list(map(int, input().split())) for _ in range(N))
    people = []
    stairs = []

    # 사람과 계단 위치 저장해두기
    for r in range(N):
        for c in range(N):
            if room[r][c] == 1:
                people.append((r, c))
            if 2 <= room[r][c] <= 10:
                stairs.append((r, c, room[r][c]))

    # 계단이 2개니까 계단마다 사람 나눠보기
    people_cnt = len(people)
    stair_set = []
    all_people = set(range(people_cnt))

    for stair_cnt in range(people_cnt+1):
        stair_one_list = list(map(set, combinations(all_people, stair_cnt)))

        for stair_one in stair_one_list:
            stair_two = all_people - stair_one
            stair_set.append((stair_one, stair_two))

    for case in stair_set:
        time = 1
        stair_time = [0] * people_cnt
        for s_idx in range(2):
            stair_len = len(case[s_idx])
            for p_idx in case[s_idx]:
                reaching_time = abs(people[p_idx][0] - stairs[s_idx][0]) + abs(people[p_idx][1] - stairs[s_idx][1])
                stair_time[p_idx] = (s_idx, reaching_time)

        stairs_wait, stairs_down = [deque(), deque()], [deque(), deque()]

        while True:
            if stair_time.count(False) == people_cnt and \
                    not (stairs_wait[0] or stairs_wait[1]) and \
                    not (stairs_down[0] or stairs_down[1]):
                break

            for p_idx in range(people_cnt):
                # 아직 계단 안갔는데
                if stair_time[p_idx]:
                    # 이분은 도착했네요
                    if time == stair_time[p_idx][1]:
                        stair_num = stair_time[p_idx][0]
                        # 대기하는 사람이 없다.
                        if not stairs_wait[stair_num]:
                            # 내려가는 사람도 없거나 3명 미만이다.
                            if not stairs_down[stair_num] or len(stairs_down[stair_num]) < 3:
                                stairs_down[stair_num].append(stairs[stair_num][2])
                            # 지금은 계단을 탈 수 없다.
                            else:
                                stairs_wait[stair_num].append(p_idx)
                        else:
                            stairs_wait[stair_num].append(p_idx)
                        stair_time[p_idx] = False
            # 계단 처리
            for stair_idx in range(2):
                # 계단을 내려가는 사람들이 있다면 내려가고있으니까 시간 내림
                if stairs_down[stair_idx]:
                    finish_cnt = 0
                    for person_idx in range(len(stairs_down[stair_idx])):
                        stairs_down[stair_idx][person_idx] -= 1
                        # 그 사람들이 다 내려갔으면 빼야됨
                        if stairs_down[stair_idx][person_idx] == 0:
                            finish_cnt += 1
                    for finish_idx in range(finish_cnt):
                        stairs_down[stair_idx].popleft()
                    # 뺐는데 대기줄 있으면 비어있는 만큼 계단으로 넣어줌
                    if stairs_wait[stair_idx]:
                        length = len(stairs_down[stair_idx])
                        for i in range(3-length):
                            stairs_down[stair_idx].append(stairs[stair_idx][2])
                            if stairs_wait[stair_idx]:
                                stairs_wait[stair_idx].popleft()
            time += 1
        answer = min(answer, time)

    print(f"#{tc+1} {answer+1}")



