# import sys
# sys.stdin = open('input.txt', 'r')
"""
다른사람 코드볼때 포인트 차감 안되는거 보고 어려운 문제가 아니구나를
깨달을 수 있었다.
자석의 번호에 따라 영향받는 순서가 다른데
마지막에 영향을 또 주긴 하지만 틀리진 않아서.. 잘 한건지 모르겠다...
(2번이 1번에 영향줬는데 1번이2번에 다시 영향줬음)
푼 시간 : 1시간 12분
메모리 : 61,720kb
실행시간 : 197ms
"""
T = int(input())

turn_order = (
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (2, 3, 1, 0),
    (3, 2, 1, 0),
    )


for tc in range(T):
    K = int(input())
    magnets = list(list(map(int, input().split())) for _ in range(4))
    for i in range(K):
        # 자석의 번호와 방향
        m_num, m_dir = map(int, input().split())
        m_idx = m_num - 1
        magnet_directions = [0] * 4 # 0 고정 1 시계 -1 반시계
        magnet_directions[m_idx] = m_dir
        # print(f"!!!!! 이번 턴에 돌릴 자석의 번호 = {m_num}  방향 = {m_dir}")
        # 돌리는 자석 번호에 따른 계산 순서
        for order in turn_order[m_idx]:
            # print(f"-------- 지금 {order+1}번째 자석 차례...")
            left, right = order-1, order+1
            # print("왼쪽 ", left+1, "오른쪽 ", right+1)
            if 0 <= left != m_idx:
                # 1번 자석이면 index가 0인데 왼쪽에 없으므로
                if magnets[left][2] != magnets[order][6]:
                    # 다른 극이면
                    magnet_directions[left] = -magnet_directions[order]
                    # print(f"극이 달라서 방향이 바뀜. 왼쪽 {left+1}번 자석의 방향 : {magnet_directions[left]}")
            if right < 4 and right != m_idx:
                # 4번 자석이면 index가 3인데 오른쪽에 없으므로
                if magnets[order][2] != magnets[right][6]:
                    magnet_directions[right] = -magnet_directions[order]
                    # print(f"극이 달라서 방향이 바뀜. 왼쪽 {right+1}번 자석의 방향 : {magnet_directions[right]}")

        # print("자석 방향 : ", magnet_directions)
        # 자석 돌리기
        for idx in range(4):
            # 시계방향
            if magnet_directions[idx] == 1:
                magnets[idx] = [magnets[idx][7]] + magnets[idx][:7]
            elif magnet_directions[idx] == -1:
                magnets[idx] = magnets[idx][1:] + [magnets[idx][0]]
            # print(f"돌아간 {idx+1} 번째 자석 모양 : ", magnets[idx])

    score = 0
    for magnet_idx in range(4):
        # print(f"{magnet_idx+1} 번 자석의 최종 모습 : ", magnets[magnet_idx])
        if magnets[magnet_idx][0]:
            score += 2 ** magnet_idx

    print(f"#{tc+1} {score}")
