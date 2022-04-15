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
        conn[ticket[0]] = set()
        if ticket[0] in left:
            if ticket[1] in left[ticket[0]]:
                left[ticket[0]][ticket[1]] += 1
            else:
                left[ticket[0]] = {ticket[1] : 1}

    # 각 티켓(FROM, TO)에 대하여
    for ticket in tickets:
        # 연결 관계를 표현하는 그래프와 같은 conn에 conn[ticket[0]]이 ticket[1]을 갖도록 한다.
        # 그렇게 하려면 conn[ticket[0]].append(ticekt[1]) 같은 로직이 있어야 하지만,
        # 딕셔너리의 특성상, 만약 conn에 ticket[0] 자체가 없는 경우에는 conn[ticket[0]]에 예외가 뜬다.
        # 그러니까 키 값이 없는 경우에도 예외없이 기본값을 반환할 수 있는 .get() 메서드를 활용한 부분임.
        # 또, OR 연산은 set() + set() 합집합 연산을 해야하는데, 여기서 + 연산자를 쓰지 않고, OR 연산자를 쓴다.
        conn[ticket[0]] = conn.get(ticket[0], set()) | set([ticket[1]])

        # 남은 티켓의 장 수를 표현하기 위한 이차원 배열, left[ticket[0]][ticket[1]] = 2
        # ticket[0]에서 ticket[1]로 가는 티켓이 2장 있다 라는 의미로 쓰는 이차원 배열을 표현해야 하지만,
        # 인덱스가 아닌 키 값을 써야 하므로 이차원 딕셔너리라는 참 기묘한 자료구조를 써야 함.
        # 아래는 그에 대한 코드
        if left.get(ticket[0]):
            left[ticket[0]][ticket[1]] = left[ticket[0]].get(ticket[1], 0) + 1
        else:
            left[ticket[0]] = {ticket[1] : 1}
    
    # 문제의 조건대로 알파벳 순으로 정렬
    for airp in conn.keys():
        conn[airp] = sorted(list(conn[airp]))
    
    # 이제 dfs
    return dfs(['ICN'], left, l, conn)