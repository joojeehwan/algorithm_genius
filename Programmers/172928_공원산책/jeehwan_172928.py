
def solution(park, routes):

    def movement(di, po):
        pass

    # 북 남 서 동
    dr = [-1, 1, 0, 1]
    dc = [0, 0, -1, 0]

    # 데이터 전처리
    order = []
    for route in routes:
        direction, distance = route.split()
        order.append((direction ,int(distance)))

    # N / M 길이 설정
    N = len(park)
    M = len(park[0])

    for row in range(N):
        for col in range(M):

            # 출발지 찾기
            if park[row][col] == 'S':

                for od_dir, od_dis in order:
                    movement(od_dir, od_dir)

    answer = []
    return answer