import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    house_i, house_j = map(int, sys.stdin.readline().split())
    stores = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        stores.append((x, y))
    goal_i, goal_j = map(int, sys.stdin.readline().split())
    stores.append((goal_i, goal_j))                 # 최종 목표도 들러야 하는 곳에 넣어줌

    # 총 50*20 == 1000 만큼의 맥주가 있음

    # 편의점을 들렀는지 확인하는 배열
    check = [0] * (n+1)

    answer = "sad"

    # bfs 시작 시작은 집에서 목표 장소까지
    q = []
    q.append((house_i, house_j))

    while q:
        now_i, now_j = q.pop(0)

        if now_i == goal_i and now_j == goal_j:     # 목표 장소에 도착하면
            answer = "happy"
            break

        for k in range(n+1):
            if check[k]:                            # 갔던 곳이면 다른 편의점으로
                continue

            next_i = stores[k][0]
            next_j = stores[k][1]

            if abs(next_i - now_i) + abs(next_j - now_j) > 1000:            # 맥주양이 부족한 거리라면 다른 편의점으로
                continue

            check[k] = 1
            q.append((next_i, next_j))


    print(answer)