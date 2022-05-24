"""
소감: 18
믿을 수가 없다........
버전을 2개를 왔다갔다 만드느라 이전 조건 때문에 걸어둔 break를
지우는 것을 잊어버리고 풀었는데
와........... 그럼 처음 테케부터 틀렸음 좋았을 것을......
그거만 아니었어도 최소 1시간 반은 고생 안해도 됐는데.....
이딴거로 멘탈 터져야한다니 ............................
창 밖에다 대고 욕하고싶다.............................
푼 시간 : 3시간 28분
메모리 : 62,756kb
실행시간 : 269ms
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
# 정지 상 우 하 좌
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

for tc in range(T):
    answer = 0
    M, A = map(int, input().split())
    route_A = list(map(int, input().split()))
    route_B = list(map(int, input().split()))
    chargers = [0] * A

    for i in range(A):
        # x, y, 범위, 충전량
        chargers[i] = list(map(int, input().split()))

    # 충전량 많은 순으로 정렬
    chargers.sort(key=lambda x:x[3], reverse=True)

    row_A, col_A, row_B, col_B = 1, 1, 10, 10

    for time in range(M+1):
        A_charger = []
        for c_idx in range(A):
            if abs(row_A-chargers[c_idx][0]) + abs(col_A-chargers[c_idx][1]) <= chargers[c_idx][2]:
                A_charger.append(c_idx)

        # B 충전기 찾기
        B_charger = []
        for c_idx in range(A):
            if abs(row_B-chargers[c_idx][0]) + abs(col_B-chargers[c_idx][1]) <= chargers[c_idx][2]:
                B_charger.append(c_idx)

        if A_charger and B_charger:
            A_energy = chargers[A_charger[0]][3]
            B_energy = chargers[B_charger[0]][3]

            A_charger_cnt, B_charger_cnt = len(A_charger), len(B_charger)

            # 둘이 쓰고싶은 제일 좋은 충전기가 같다면
            if A_charger[0] == B_charger[0]:
                # 둘 다 1개라면
                if A_charger_cnt == 1 and B_charger_cnt == 1:
                    # 걍 B가 빠져라
                    B_energy = 0
                # A는 1개인데 B는 여러개라면
                elif A_charger_cnt == 1 and B_charger_cnt > 1:
                    # B가 다음거 먹어라
                    B_energy = chargers[B_charger[1]][3]
                # B는 1개인데 A는 여러개라면
                elif B_charger_cnt == 1 and A_charger_cnt > 1:
                    A_energy = chargers[A_charger[1]][3]
                # 둘 다 여러개라면
                elif A_charger_cnt > 1 and B_charger_cnt > 1:
                    # 둘 중에 두번째 충전량이 더 많은 놈으로 추가하자
                    if chargers[A_charger[1]][3] > chargers[B_charger[1]][3]:
                        A_energy = chargers[A_charger[1]][3]
                    else:
                        B_energy = chargers[B_charger[1]][3]
            answer += A_energy + B_energy
        # 둘 중 하나만 있는 경우
        elif not A_charger and B_charger:
            answer += chargers[B_charger[0]][3]
        elif A_charger and not B_charger:
            answer += chargers[A_charger[0]][3]
        if time >= M:
            break
        row_A += dx[route_A[time]]
        col_A += dy[route_A[time]]
        row_B += dx[route_B[time]]
        col_B += dy[route_B[time]]

    print(f"#{tc+1} {answer}")
