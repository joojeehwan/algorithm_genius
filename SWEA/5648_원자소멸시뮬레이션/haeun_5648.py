# import sys
# sys.stdin = open('input.txt', 'r')
"""
예시에 1.5초에 충돌이 있어서 x, y 좌표를 2배씩 늘리고 0.5초씩 슬로우로 본다고 침
어차피 걸린 시간을 구하는 것도 아니니까 상관 없다고 생각.
-2000에서 2000까지 4000초를 다 돌려고 했는데, x와 y의 각각 최소 최대를 구하고
x와 y중 차이가 더 큰 값을 기준으로 돌아도 충분하지 않을까 라는 생각이 들었음
푼 시간 : 2시간 40분 ㅋㅋ
메모리 : 105,268kb
실행시간 : 8,104ms
"""



T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for tc in range(T):
    N = int(input())
    answer = 0
    atoms = []
    x_min, x_max, y_min, y_max = 1001, -1001, 1001, -1001

    for _ in range(N):
        atom = list(map(int, input().split()))
        x_min = min(x_min, atom[0])
        x_max = max(x_max, atom[0])
        y_min = min(y_min, atom[1])
        y_max = max(y_max, atom[1])

        atom[0] *= 2
        atom[1] *= 2
        atoms.append(atom)

    # gap도 2배
    gap = (max(x_max-x_min, y_max-y_min))*2

    for halt_sec in range(gap):
        positions = dict()
        for idx in range(N):
            if atoms[idx]:
                direct = atoms[idx][2]
                atoms[idx][0] += dx[direct]
                atoms[idx][1] += dy[direct]
                atom_pos = (atoms[idx][0], atoms[idx][1])

                if atom_pos in positions:
                    # 이미 있는 위치면 원자의 index 추가
                    positions[atom_pos].append(idx)
                else:
                    positions[atom_pos] = [idx]

        # 위치(key)마다 원자의 index를 배열(value)로 저장
        for pos in positions:
            # 한 위치에 원자가 2개 이상 = 충돌
            if len(positions[pos]) > 1:
                # 그 위치의 원자들 다 보면서 에너지 계산
                for atom_idx in positions[pos]:
                    answer += atoms[atom_idx][3]
                    atoms[atom_idx] = False



    print(f"#{tc+1} {answer}")

