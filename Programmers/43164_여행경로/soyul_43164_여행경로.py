def solution(tickets):
    used = [0] * len(tickets)
    possible = []

    def dfs(start, route):

        if len(route) == len(tickets) + 1:      # 모든 도시를 다 방문하면
            possible.append(route)

        for i in range(len(tickets)):
            if used[i]:  # 이미 확인한 곳이면
                continue

            if tickets[i][0] == start:  # 새로운 출발지
                used[i] = 1
                dfs(tickets[i][1], route + [tickets[i][1]])
                used[i] = 0

        if len(route) == len(tickets) + 1:      # 모든 도시를 다 방문하면
            possible.append(route)

    # 무조건 ICN 부터 시작
    routes = ["ICN"]
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':      # ICN 티켓이면 dfs 검사
            used[i] = 1
            dfs(tickets[i][1], routes + [tickets[i][1]])
            used[i] = 0

    possible.sort()     # 가능한 루트 중 알파벳 순서로

    return possible[0]