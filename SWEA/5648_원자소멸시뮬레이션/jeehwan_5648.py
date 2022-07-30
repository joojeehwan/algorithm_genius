'''

(1) atmos에 현재 원자들의 상태를 저장

(2) 이동시킨다

- 범위 밖이면 삭제한다 (이동할 때 원자가 범위 밖에서 만나는 경우는 없으므로)

- 범위 안이면 check_atoms 에 저장하고, 바뀐 위치를 새롭게 atmos에 저장한다

(이때 check_atoms는 dictionary형태로, key값을 (행,열)과 같은 튜플형태로 하는 갖는 자료형이다.)



(3)check_atoms를 전부 조사하여 해당 위치에 두개이상의 원자가 있으면 atmos를 삭제한다.

※시간 초과가 날것을 걱정해서 격자를 사용했지만, 격자때문에 메모리 초과가 났다. 격자를 이용하면 해당위치를 즉시 확인할 수 있기 때문에 속도는 빠르지만 메모리가 초과할 수 있다는 트레이드 오프가 있다. 이를 정확히 인지하고 무조건 격자를 사용하지 않도록 주의한다.

시간복잡도는

원자가 한쪽구석에서 반대쪽 구석으로 가는 경우(4000)*원자의 최대개수(1000)=O(4000*1000)이므로 충분히 해결할 수 있다.

'''
'''
2
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9

1
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
'''
from collections import deque
T = int(input())
#상 하 좌 우,,, 문제에 주어진 dir에 맞게! x, y라고 해서 row, col 헷갈리지 말기!
dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]


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
        de = 1
        for _ in range(size):
            #원래 있던 곳을 삭제
            atom_index, row, col, dir, energy = atoms.popleft()
            # 새로 갈곳을 가자!
            next_row = row + dr[dir]
            next_col = col + dc[dir]
            #이동후 범위 체크
            if 0<= next_row < 4001 and 0<= next_col < 4001:
                #바뀐 위치를 새롭게 저장
                atoms.append([atom_index, next_row, next_col, dir, energy])
                #딕셔너리에 저장
                if (next_row, next_col) in check_atoms:
                    #값이 이미 있다면 추가
                    check_atoms[(next_row, next_col)].append([atom_index, dir, energy])
                else:
                    #새로운 값이면,,!
                    check_atoms[(next_row, next_col)] = [[atom_index, dir, energy]]
        #값이 2개 이상인것
        print(check_atoms)
        #key (좌표1, 좌표2)의 형태!
        for key in check_atoms:
            # print(tup)
            # value들이 2개이상 모여서 터지게 될때!
            if len(check_atoms[key]) >= 2:
                #모인 녀석들의 갯수 만큼! for문 돌리면서!
                for atom_index, dir, energy in check_atoms[key]:
                    #소멸 시키고!
                    atoms.remove([atom_index, key[0], key[1], dir, energy])
                    ans += energy

    print("#%d %d" % (tc, ans))