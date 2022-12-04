'''


마법사상어와 파이어볼 관련해서, 푼 다음에 어떤식으로 풀었는지 비교

'''

#이전 풀이



N, M , K = map(int, input().split())
atoms = []



for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    atoms.append([r-1, c-1, m, s, d])



# 해당 (row, col)에 있는 mass / speed / dir을 담는다.
MAP = [[[] for _ in range(N)] for _ in range(N)]

#상 부터 오른쪽으로 순서대로 8방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


for _ in range(K):

    #1. 모든 원자는 1초가 지날 때마다 자신의 방향으로 자신의 속력만큼 이동
    while atoms:

        cr, cc, cm, cd, cs = atoms.pop(0)
        #연결되어 있음을 모듈려 연산으로 구현
        next_row = (cr + cs * dr[cd]) % N
        next_col = (cc + cs * dc[cd]) % N
        MAP[next_row][next_col].append([cm, cs, cd])


    #이동이 끝난 이후에, 2개 이상의 원자가 있는 곳에 합성이 일어남

    #우선, 2개 이상인지 check 먼저

    for row in range(N):
        for col in range(N):

            # 2개 이상의 원자들이 한 row, col에 있음.
            # []의 형태로 append 했으니깐! len으로 확인 할 수 있음
            # 처음부터 MAP의 자료구조 형태를 [[[], [], [], ]] 로 했기에 가능한 것
            if len(MAP[row][col]) > 1 :

                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[row][col])


                #해당 row, col에 있는 각각의 원자들을 하나씩 검사
                while MAP[row][col] :

                    _m, _s, _d = MAP[row][col].pop(0)
                    sum_m += _m
                    sum_s += _s
                    #각각의 원자의 방향이 어떻게 구성되는지 확인하기 위한 작업
                    if _d % 2: #상 하 좌 우 중에 하나
                        cnt_odd += 1

                    else:   # 대각선 방향 중에 하나
                        cnt_even += 1

                # 합쳐진 방향이 모두 상하좌우/대각선이면 -> 상하좌우 중 하나의 값 통일
                # 위에 case가 아니라면, 대각선의 4방향 할당
                if cnt == cnt_odd or cnt == cnt_even :
                    nd = [0,2,4,6]

                else :
                    nd = [1,3,5,7]

                #질량이 0인 원소는 소멸 되기에..!
                if sum_m // 5 :
                    #4방향으로 나뉘어진다.
                    for d in nd:
                        atoms.append([r, c, sum_m // 5, sum_s // cnt, d])

            #이거 왜 하는 거지?!
            '''
            알려줘잉..
            
             atoms에 들어가는 자료구조의 형태를 확인하라
             해당 row, col, mass, speed, dir을 넣어야 함.
             그걸 넣기 위한 것
             딱 하나여도, pop 하고 다시 넣어야, 다음번의 반복에서 다음 칸으로 갈 수 있으니깐 
            
            '''
            if len(MAP[row][col]) == 1:
                atoms.append([row, col] + MAP[row][col].pop())

print(sum([at[2] for at in atoms]))









#코드트리 해설


# 변수 선언 및 입력:

n, m, k = tuple(map(int, input().split()))

grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

next_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def next_pos(x, y, v, move_dir):
    dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]

    # 움직인 이후 값이 음수가 되는 경우, 이를 양수로 쉽게 만들기 위해서는
    # n의 배수이며 더했을 때 값을 항상 양수로 만들어 주는 수인 nv를 더해주면 됩니다.
    nx = (x + dxs[move_dir] * v + n * v) % n
    ny = (y + dys[move_dir] * v + n * v) % n

    return (nx, ny)


def move_all():
    for x in range(n):
        for y in range(n):
            for w, v, move_dir in grid[x][y]:
                next_x, next_y = next_pos(x, y, v, move_dir)
                next_grid[next_x][next_y].append(
                    (w, v, move_dir)
                )


def split(x, y):
    sum_of_mass, sum_of_velocity = 0, 0
    num_of_dir_type = [0, 0]

    for w, v, move_dir in next_grid[x][y]:
        sum_of_mass += w
        sum_of_velocity += v
        num_of_dir_type[move_dir % 2] += 1

    start_dir = -1
    # 전부 상하좌우 방향이거나, 전부 대각선 방향으로만 이루어져 있다면
    # 각각 상하좌우 방향을 갖습니다.
    if not num_of_dir_type[0] or not num_of_dir_type[1]:
        start_dir = 0
    # 그렇지 않다면, 각각 대각선 방향을 갖습니다.
    else:
        start_dir = 1

    atom_cnt = len(next_grid[x][y])

    # 각 방향 갖는 원자를 추가해줍니다.
    for move_dir in range(start_dir, 8, 2):
        # 질량이 0보다 큰 경우에만 추가합니다.
        if sum_of_mass // 5 > 0:
            grid[x][y].append(
                (sum_of_mass // 5,
                 sum_of_velocity // atom_cnt,
                 move_dir)
            )


def compound():
    # Step1. grid값을 초기화합니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = list()

    # Step2. 합성을 진행합니다.
    for i in range(n):
        for j in range(n):
            atom_cnt = len(next_grid[i][j])
            if atom_cnt == 1:
                grid[i][j].append(next_grid[i][j][0])
            # 2개 이상인 경우에는 분열됩니다.
            elif atom_cnt > 1:
                split(i, j)


def simulate():
    # Step1. next_grid를 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = list()

    # Step2. 원자들을 전부 움직입니다.
    move_all()

    # Step3. 합성이 일어나고, 그 결과를 grid에 저장합니다.
    compound()


for _ in range(m):
    x, y, m, s, d = tuple(map(int, input().split()))
    grid[x - 1][y - 1].append((m, s, d))

# k초에 걸쳐 시뮬레이션을 반복합니다.
for _ in range(k):
    simulate()

ans = sum([
    weight
    for i in range(n)
    for j in range(n)
    for weight, _, _ in grid[i][j]
])

print(ans)