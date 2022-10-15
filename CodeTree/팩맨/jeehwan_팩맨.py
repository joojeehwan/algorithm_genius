'''

만들어야 하는 함수


1) 몬스터 이동

2) 팩맨 이동

3) 몬스터 시체 소멸

4) 목스터 복제


이거 마법사상어와 복제와 비슷하다 이거 풀고, 복제도 다시 한번 바라보자.


sol)

몬스터 하나 하나를 전부 관리하게 되면, 총 몬스터의 수를 m이라 했을 떄 m개의 몬스터들을 매 초마다 한 칸씩 이동 시켜줘야 하므로...! => 시간 초과가 될 수도...!

그래서

몬스터의 수가 많다고 해도, 결국 (위치, 바라보고 있는 방향)이 일치하는 몬스터들의 움직임은 정확히 동일

따라서 동일한 위치에서, 동일한 방향을 바라보고 있는 몬스터 수 자체를 관리하는 식으로 시뮬레이션 진행

시체 자체에 대한 처리를 깔끔하게 하기 위해서, 매 초마다 몬스터가 몇 마리씩 있었는지 전부 저장하여 관리

따라서 monster[t][row][col][move_dir] => "t초 이후에, 위치 (row, col)에서 move_dir을 바라고 있는 몬스터의 수"

시체가 2번 턴을 거쳐야 삭제되는 부분은

dead[row][col][t]라는 배열을 만들어, "(row, col) 위치에서 썩는데 t번의 턴이 남은 몬스터의 수"
'''


# 이 값의 존재 이유를 이따 알아보자.
MAX_T = 25
MAX_N = 4
DIR_NUM = 8
P_DIR_NUM = 4
MAX_DECAY = 2

# 변수 선언 및 입력

n = 4

# 몬스터의 마리 수 m
# 게임 횟수 t

m, t = map(int, input().split())

#팩맨의 위치 저장하기

p_row, p_col = map(int, input().split())

# 인덱스로 변환 하기 위함.  // ; 를 사용해서 한줄에 모두 적기 -> 가시성
p_row -= 1; p_col -= 1

# 몬스터 8방향 상, 좌상, ... , 우상
m_dr = [-1, -1, 0, 1, 1, 1, 0, -1]
m_dc = [0, -1, -1, -1, 0, 1, 1, 1]

# 팩맨 이동 방향 => 이것도 정해져 있음. 팩맨의 우선순위
# 상 좌 하 우
p_dr = [-1, 0, 1, 0]
p_dc = [0, -1, 0, 1]



# 둘의 차이 확인하기

# 이건 2차원 배열로 기록 하는 것이 아님 격자를 형상화 해서 넣는 것이 아님.
# monster[t][row][col][move_dir] => "t초 이후에, 위치 (row, col)에서 move_dir을 바라고 있는 몬스터의 수"
# 1초 부터 시작이라 MAX_T + 1 을 한 것.
monster = [[[[0] * DIR_NUM for _ in range(n)] for _ in range(n)] for _ in range(MAX_T + 1)]

for _ in range(m):
    # 첫 번 째 턴의 상태를 기록
    monster_row, monster_col, monster_dir = map(int, input().split())
    monster[0][monster_row - 1][monster_col - 1][monster_dir - 1] += 1

# 이차원 배열인데, 각 row, col 에 해당하는 것이 값 하나가 아니라, 배열로 이루어진 것.
# t (초) 가 1 부터 시작해서, 그걸 맞추기 위해서 MAX_DACAY + 1 을 한 것. 1부터 인덱스 사용하니 하나더 필요 한 것!

# (row, col) 위치에서 썩는데 t번의 턴이 남은 몬스터의 수
# 0, 1(x) => 0, 1, 2 (1초, 2초)
# dead[row][col][1] 은 딱 내가 갔을 때 시체가 있고 없고의 여부
dead = [[[0] * (MAX_DECAY + 1) for _ in range(n)] for _ in range(n)]
# t가 인덱스가 줄수록 기간이 줄어들고 있는 것

#print(monster)

# #이건 그냥, [[1, 3, 5], [2, 2, 7], [3, 4, 6], [4, 2, 2]] 이렇게 넣는 것.
# monster = [list(map(int, input().split())) for _ in range(m)]

#현재 몇 번 째 턴인지 저장
t_num = 1


# 몬스터 이동

def move_monster () :

    # 각 (row, col)칸에 dir 방향을 보고 있는 몬스터들이
    # 그 다음으로 이동해야할 위치 및 방향을 구해
    # 전부 (칸, 방향)을 위동
    # 이 작업을 일일이 몬스터 마다 위치를 구해서 이동시키면 시간 초과

    for row in range(n):
        for col in range(n):
            for dir in range(DIR_NUM) :

                # 몬스터들이 다음 이동할 방향
                # 현재 위치에서, 45도씩 회전 하면서, 판단, 8방향을 다 보고, 그떄도 없으면 가만히 있기
                for m_dir in range(DIR_NUM):
                    next_dir = (dir + m_dir + DIR_NUM) % DIR_NUM
                    next_row = row + m_dr[next_dir]
                    next_col = col + m_dc[next_dir]

                    # 범위 생각, 팩맨이 있으면 안가고, 몬스터의 시체가 있으면 가지 않는다.
                    # 팩맨이 있으면 안가고?! 이걸 (row, col) != (row, col) 이렇게 하는 건 좋다.  메모
                    # 위에 초기 입력 받을 때 for 문에서 monster[0][row][col][dir]로 받았다. 따라서, 초기 맵의 t_num = 0 이고, 우리 초기 시작 t_num은 1이니
                    # 아래와 같이 적어서, 초기에서 다음 t_num으로 이동을 하는 것
                    if (0 <= next_row < n and 0 <= next_col < n) and ((next_row, next_col) != (p_row, p_col)) and (dead[next_row][next_col][0] == 0 and dead[next_row][next_col][1] == 0) :
                        monster[t_num][next_row][next_col][next_dir] += monster[t_num - 1][row][col][dir]

                    else:
                        monster[t_num][row][col][dir] += monster[t_num - 1][row][col][dir]

# 팩맨 이동

def move_packman():

    max_kill = -1
    best_route = (-1, -1, -1)

    global p_row, p_col
    # "상 좌 하 우"의 우선순위를 가지고 탐색해야 함.
    #우선순위 순서대로 수행. 따라서 위에 델타 배열 설정할 때 부터, 우선순위대로 설정함.
    # 가장 최적의 경로를 탐색 하는 부분
    for dir1 in range(P_DIR_NUM):
        for dir2 in range(P_DIR_NUM):
            for dir3 in range(P_DIR_NUM):
                pack_man_row, pack_man_col = p_row, p_col
                kill = 0

                #방문여부 조사
                visited = []

                #상 좌 하 우 우선순대로, dir을 돌리면서 확인 => 자연스럽게 총 3칸 이동이 이루어짐
                for move_dir in [dir1, dir2, dir3]:
                    next_pack_man_row = pack_man_row + p_dr[move_dir]
                    next_pack_man_col = pack_man_col + p_dc[move_dir]

                    #범위 체크
                    if 0 <= next_pack_man_row < n and 0 <= next_pack_man_col < n :
                        # 이미 간곳은 가지 않는다.
                        if (next_pack_man_row, next_pack_man_col) not in visited:
                            kill += sum(monster[t_num][next_pack_man_row][next_pack_man_col])
                            visited.append((next_pack_man_row, next_pack_man_col))

                    # 팩맨 이동 (실제 이동은 아님)
                    pack_man_row = next_pack_man_row
                    pack_man_col = next_pack_man_col

                if kill > max_kill:
                    max_kill = kill
                    best_route = (dir1, dir2, dir3)

    # 실제로 몬스터 죽이기
    d1, d2, d3 = best_route

    for move_dir in [d1, d2, d3]:
        next_p_row = p_row + p_dr[move_dir]
        next_p_col = p_col + p_dc[move_dir]

        for i in range(DIR_NUM):
            #원래 딱 처음에 죽으면, 가장 기간이 많이 남은게 맞으니깐
            dead[next_p_row][next_p_col][MAX_DECAY] += monster[t_num][next_p_row][next_p_col][i]
            monster[t_num][next_p_row][next_p_col][i] = 0

        p_row, p_col = next_p_row, next_p_col


#시체 시간 경과
def decay_m():
	# decay를 진행합니다. 턴을 하나씩 깎아주면 됩니다.
    for i in range(n):
        for j in range(n):
            for k in range(MAX_DECAY):
                dead[i][j][k] = dead[i][j][k + 1]
            #max가 있는 곳을 0으로 만들기
            dead[i][j][MAX_DECAY] = 0

# 몬스터 복제
def monster_copy () :

    # 현재 시간 기준으로 몬스터 복제
    for row in range(n):
        for col in range(n):
            for k in range(DIR_NUM):
                # 한턴 뒤에 생성 되니 한턴 전에 있던 것을 복제해 온다.
                # 일단 기존에 몬스터는 초기 입력받을 떄 다 받았으니깐
                monster[t_num][row][col][k] += monster[t_num - 1][row][col][k]


def simulate():
    # 매 초마다 기록하기 때문에 굳이 copy를 진행할 필요는 없습니다.

    # 각 칸에 있는 몬스터를 이동시킵니다.
    move_monster()

    # 팩맨을 이동시킵니다.
    move_packman()

    # 시체들이 썩어갑니다.
    decay_m()

    # 몬스터가 복제됩니다.
    monster_copy()


def count_monster():
    cnt = 0

    # 마지막 턴을 마친 이후의 몬스터 수를 셉니다.
    for i in range(n):
        for j in range(n):
            for k in range(DIR_NUM):
                cnt += monster[t][i][j][k]

    return cnt


# t번 시뮬레이션을 진행합니다.
while t_num <= t:
	simulate()
	t_num += 1

print(count_monster())