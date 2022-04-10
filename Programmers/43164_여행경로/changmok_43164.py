# dfs를 돌아 처음 끝까지 닿는 경로를 반환
def dfs(route, left, l, conn):
    if len(route) == l + 1:
        return route
    last = route[-1]
    if last in conn:
        for nxt in conn[last]:
            if not left[last][nxt]:
                continue
            left[last][nxt] -= 1
            able = dfs(route + [nxt], left, l, conn)
            if able:
                return able
            left[last][nxt] += 1
        

def solution(tickets):
    l = len(tickets)
    conn = {}
    left = {}
    
    # 그래프와 같은 식으로 연결 관계를 저장
    # 정수 인덱스를 쓸 수 없으니 문자열을 인덱스처럼 쓸 수 있는 딕셔너리 형태
    for ticket in tickets:
        conn[ticket[0]] = conn.get(ticket[0], set()) | set([ticket[1]])
        if left.get(ticket[0]):
            left[ticket[0]][ticket[1]] = left[ticket[0]].get(ticket[1], 0) + 1
        else:
            left[ticket[0]] = {ticket[1] : 1}
    
    # 문제의 조건대로 알파벳 순으로 정렬
    for airp in conn.keys():
        conn[airp] = sorted(list(conn[airp]))
    
    # 이제 dfs
    return dfs(['ICN'], left, l, conn)