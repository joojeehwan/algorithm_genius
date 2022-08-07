# global로 쓰기 위해
uf = []


def find(a):
    global uf
    if uf[a] < 0: return a # 나의 부모는 없다!
    uf[a] = find(uf[a])
    return uf[a]


def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    # 둘이 같은 그룹에 있다면 그냥 반환
    if pa == pb: return
    # a에 얼마나 연결되었는지 확인하기 위해 -1 을 더한다.
    uf[pa] += uf[pb]
    uf[pb] = pa


def solution(n, wires):
    global uf
    answer = 987654321

    for i in range(n-1):
        # 탑의 개수만큼 -1로 채운 배열 생성, 부모를 저장하는 배열
        uf = [-1 for _ in range(n+1)]
        # 선을 하나씩 끊는다(끊은 연결 제외하고 전선 배열 복사)
        tmp = [wires[x] for x in range(n-1) if x != i]
        for a, b in tmp:
            # union find를 통해 탑끼리 연결
            merge(a, b)
        # 본인이 - 값이면 조상이므로, 그 조상에 몇개 연결되었는지 차이 구함
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))