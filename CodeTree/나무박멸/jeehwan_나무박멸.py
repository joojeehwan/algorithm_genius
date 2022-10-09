'''
함수 3개 만들기

1. 나무 성장
각 칸 마다, for문 돌려서, 근처에 있는 나무의 갯수 만큼 해당 칸의 나무 갯수 증가.

2. 번식
"모든 나무에서 동시에 일어남." => 임시 배열 테이블이 필요함.

- 벽(-1), 다른 나무(1~100), 제초제 없는 곳에 번식

- 나무가 있는 칸 마다 for문으로 인접(상하좌우)한 번식이 가능한 칸의 수만큼 // 연산

- 나무의 번식은 다른 칸으로 부터 중복이 가능

3. 제초제 뿌리기

- 가장 많이 제초제가 박멸되는 칸에 제초제를 뿌린다.

나무가 있는 칸 마다, k칸 만큼 대각선 방향으로 제초제를 뿌린다.

그 갯수가 가장 큰 것을 골라서 뿌린다.  대각선 4방향으로 뿌리고,

벽이 있거나, 나무가 끊겨 있으면 뿌리지 않는다.

c년 동안 유지되다. c + 1년에 사라짐.(다시 뿌려질때마다 다시 c년으로 갱신)

'''


n, m, k, c = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

ans = 0
#제초제 배열
herbicide = [[0] * n for _ in range(n)]

#인접 4방향 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#대각 4방향 좌상, 좌하, 우상, 우하
dir_dr = [-1, 1, -1, 1]
dir_dc = [-1, -1, 1, 1]


# 성장
'''
1. 나무 성장
각 칸 마다, for문 돌려서, 근처에 있는 나무의 갯수 만큼 해당 칸의 나무 갯수 증가.
'''
def tree_grow() :

    for row in range(n):
        for col in range(n):
            if MAP[row][col] <= 0:
                continue

            temp_tree = 0
            for k in range(4):
                next_row = row + dr[k]
                next_col = col + dc[k]

                #우선 범위 확인
                if 0<= next_row < n and 0 <= next_col < n:
                    # 인접한 4방향 중에 나무가 있는 곳만
                    if MAP[next_row][next_col] > 0:
                        temp_tree += 1

            #인접한 4방향에 나무가 있는 만큼 성장
            MAP[row][col] += temp_tree

#번식
'''
2. 번식
"모든 나무에서 동시에 일어남." => 임시 배열 테이블이 필요함.

- 벽(-1), 다른 나무(1~100), 제초제 없는 곳에 번식 => 즉 아무도 없는 칸에서 번식을 시작.

- 나무가 있는 칸 마다 for문으로 인접(상하좌우)한 번식이 가능한 칸의 수만큼 // 연산

- 나무의 번식은 다른 칸으로 부터 중복이 가능
'''

def tree_breed() :

    new_MAP = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            #번식할 나무 선택
            if MAP[row][col] <= 0 :
                continue

            temp_tree = 0
            # 해당 나무와 인접한 나무 중에 아무도 없는 칸의 갯수
            for k in range(4):

                next_row = row + dr[k]
                next_col = col + dc[k]

                #범위
                if 0<= next_row < n and 0 <= next_col < n:
                    # 조건 (제초제 없고)
                    if herbicide[next_row][next_col]:
                        continue
                    # 조건 (나무 없고, 벽 없고)
                    if MAP[next_row][next_col] == 0:
                        temp_tree += 1

            #아무도 없는 칸의 개수를 기반으로 // 연산을 통해서 본격적인 번식을 시작
            for k in range(4):
                next_row = row + dr[k]
                next_col = col + dc[k]

                if 0 <= next_row < n and 0 <= next_col < n:

                    if herbicide[next_row][next_col]:
                        continue

                    if MAP[next_row][next_col] == 0:
                        new_MAP[next_row][next_col] += MAP[row][col] // temp_tree


    # return new_MAP
    #동시에 번식을 진행
    for row in range(n):
        for col in range(n):
            MAP[row][col] += new_MAP[row][col]


# 제초제

'''

- 가장 많이 제초제가 박멸되는 칸에 제초제를 뿌린다.

나무가 있는 칸 마다, k칸 만큼 대각선 방향으로 제초제를 뿌린다.

그 갯수가 가장 큰 것을 골라서 뿌린다.  대각선 4방향으로 뿌리고,

벽이 있거나, 나무가 끊겨 있으면 뿌리지 않는다.

c년 동안 유지되다. c + 1년에 사라짐.(다시 뿌려질때마다 다시 c년으로 갱신)

'''
def tree_weed() :

    global ans

    #가장 많이 뿌려지는 곳의 양과 좌표를 구하자.
    max_weed, max_row, max_col = 0, 0, 0
    for row in range(n):
        for col in range(n):
            
            #나무가 있는 모든 칸에 제초제를 뿌리자
            
            #나무 없는 곳, 벽 거르기
            if MAP[row][col] <= 0 :
                continue

            #일단 자기 자신도 제초제 뿌리고 시작하니깐
            temp_max_weed = MAP[row][col]

            #대각선 방향으로, k만큼 제초제를 뿌리는 것
            for dr, dc in zip(dir_dr, dir_dc):
                next_row = row
                next_col = col
                #k 만큼 대각선의 방향으로 제초제를 뿌린다.
                for _ in range(k):
                    next_row = next_row + dr
                    next_col = next_col + dc

                    if 0<= next_row < n and 0 <= next_col < n :

                        #벽이 있거나, 나무가 없으면 뿌리지 않는다.
                        # break를 통해, 아예 그 대각선 방향으로 제초제를 뿌리는 것을 멈춘다.
                        if MAP[next_row][next_col] <= 0 :
                            break

                        temp_max_weed += MAP[next_row][next_col]

            if max_weed < temp_max_weed:
                max_weed = temp_max_weed
                max_row = row
                max_col = col

    #정답 갱신
    ans += max_weed

    #찾은 칸에 제초제를 뿌린다. => 실제 나무 삭제
    MAP[max_row][max_col] = 0
    herbicide[max_row][max_col] = c

    for dir in range(4):
        next_row = max_row
        next_col = max_col

        for _ in range(k):
            next_row = next_row + dir_dr[dir]
            next_col = next_col + dir_dc[dir]

            if 0 <= next_row < n and 0 <= next_col < n :

                #나무가 끊긴 곳이면 가지 않아.
                if MAP[next_row][next_col] < 0 :
                    break

                # 나무가 없지만, 제초제 기록은 있을 수 있다.
                if MAP[next_row][next_col] == 0:
                    herbicide[next_row][next_col] = c
                    break
                    
                #나무가 있어서 제초하고, 제초제 기록을 남기기

                MAP[next_row][next_col] = 0
                herbicide[next_row][next_col] = c


def down_weed():
    for row in range(n):
        for col in range(n):
            if herbicide[row][col] > 0 :
                herbicide[row][col] -= 1


for _ in range(m):

    #성장
    tree_grow()
    #번식
    # new_MAP = tree_breed()
    # MAP = new_MAP
    tree_breed()
    #제초제
    down_weed()
    tree_weed()

print(ans)
