'''

(1) atomD에 현재 원자들의 상태와 상태를 저장한다



(2) 이동시킨다

- 범위 밖이면 삭제한다 (이동할 때 원자가 범위 밖에서 만나는 경우는 없으므로)

- 범위 안이면 cheakD에 저장하고, 바뀐 위치를 새롭게 atomD에 저장한다

(이때 cheakD는 dictionary형태로, key값을 (행,열)과 같은 튜플형태로 하는 갖는 자료형이다.)



(3) cheakD를 전부 조사하여 해당 위치에 두개이상의 원자가 있으면 atomD를 삭제한다.

※시간 초과가 날것을 걱정해서 격자를 사용했지만, 격자때문에 메모리 초과가 났다. 격자를 이용하면 해당위치를 즉시 확인할 수 있기 때문에 속도는 빠르지만 메모리가 초과할 수 있다는 트레이드 오프가 있다. 이를 정확히 인지하고 무조건 격자를 사용하지 않도록 주의한다.

시간복잡도는

원자가 한쪽구석에서 반대쪽 구석으로 가는 경우(4000)*원자의 최대개수(1000)=O(4000*1000)이므로 충분히 해결할 수 있다.

​


'''


# from numba.cuda import atomic
#
# MAP = [[0 for _ in range(4001)] for _ in range(4001)]
#
# T = int(input())
#
# for tc in range(1, T + 1):
#
#     #상 하 좌 우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     atom_list = []
#     length = int(input())
#     remove_list = set()
#     energy_sum = 0
#
#     for _ in range(length):
#         x, y, dir, energy = map(int, input().split())
#         x = (x + 1000) * 2
#         y = (y + 1000) * 2
#         atom_list.append([y, x, dir, energy])
#         MAP[y][x] += 1
#         pop_list = []
#
#     while atom_list:
#         for i in range(len(atom_list)):
#             y, x, dir, energy = atom_list[i]
#             move_y = y + dy[dir]
#             move_X = x + dx[dir]
#             #MAP 밖으로 가면

from collections import deque
T = int(input())
#상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):

    N = int(input())
    atoms = deque([])
    for i in range(N):
        x, y, dir, energy = map(int, input().split())
        row = 2 * x + 2000
        col = 2 * y + 2000
        atoms.append([i, row, col, dir, energy])
    # print(atoms)
    ans = 0
    while atoms:
        check_atoms = {}
        size = len(atoms)
        #원자 움직이기
        for _ in range(size):
            #원래 있던 곳을 삭제
            atom_index, row, col, dir, energy = atoms.popleft()
            # 새로 갈곳을 가자!
            next_row = row + dr[dir]
            next_col = col + dc[dir]
            #이동후 범위 체크
            if 0<= next_row < 4001 and 0<= next_col < 4001:
                atoms.append([atom_index, next_row, next_col, dir, energy])
                if (next_row, next_col) in check_atoms:
                    #값이 이미 있다면 추가
                    check_atoms[(next_row, next_col)].append([atom_index, dir, energy])
                else:
                    #새로운 값이면,,!
                    check_atoms[(next_row, next_col)] = [[atom_index, dir, energy]]

        for tup in check_atoms:
            if len(check_atoms[tup]) >= 2:
                for atomNum, d, k in check_atoms[tup]:
                    atoms.remove([atomNum, tup[0], tup[1], d, k])
                    ans += k

    print("#%d %d" % (tc, ans))