import heapq


def dijkstra(begin, goal):
    hq = []
    heapq.heappush(hq, (0, begin))
    times = [roads_num * 2 * 100] * (students_num + 1)  # begin 학생이 각 마을로 가는 소요시간 리스트
    times[begin] = 0
    while hq:
        time, now = heapq.heappop(hq)  # 누적 소요시간, 현재 위치
        # now로 가는 기존 방법이 더 빠름
        if time > times[now]:
            continue
        for new_time, new in roads[now]:  # 여기서 이어진 도로들 중
            # new로 가는 새로운 방법이 더 빠름
            if time + new_time < times[new]:
                times[new] = time + new_time  # new 마을로 가는 데 걸리는 최소 소요시간
                heapq.heappush(hq, (times[new], new))
    return times[goal]


students_num, roads_num, place = map(int, input().split())  # 학생(마을) 수, 단방향 도로 수, 모이는 마을
roads = [[] for _ in range(students_num + 1)]  # 도로 리스트 (시작점, 끝점, 소요시간)
for i in range(roads_num):
    s, e, t = map(int, input().split())
    roads[s].append((t, e))


ans = 0
for student in range(1, students_num + 1):
    # student에서 place로 갔다가 다시 student로 돌아오는 소요 시간
    cost = dijkstra(student, place) + dijkstra(place, student)
    ans = max(ans, cost)
print(ans)