from collections import deque


T = int(input())  # 테스트케이스
for _ in range(T):
    stores = int(input())  # 가게 수
    start = tuple(map(int, input().split()))  # 시작 지점(상근이네 집)
    store_lst = []  # 편의점 좌표 목록
    for __ in range(stores):
        store_lst.append(tuple(map(int, input().split())))
    end = tuple(map(int, input().split()))  # 도착 지점(락 페스티벌)

    # BFS
    visited = [0] * stores  # 방문한 상점 표시
    queue = deque()
    queue.append(start)
    while queue:
        now_r, now_c = queue.popleft()
        if abs(now_r - end[0]) + abs(now_c - end[1]) <= 1000:  # 도착지점에 도달 가능
            print('happy')
            break
        for i in range(stores):
            if not visited[i]:
                new_r, new_c = store_lst[i]
                if abs(now_r - new_r) + abs(now_c - new_c) <= 1000:  # 다음 상점에 도달 가능
                    queue.append((new_r, new_c))
                    visited[i] = 1
    else:
        print('sad')