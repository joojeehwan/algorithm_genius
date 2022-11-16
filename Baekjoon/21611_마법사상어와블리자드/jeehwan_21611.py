'''


마법사 상어 시리즈

마법사 상어와 블리자드


"파괴"가 다 끝나고, "폭발"이 맞는것이 아님

파괴 -> 폭발 하나의 시퀀스로 이루어짐.



1. 입력에 의한 구슬 "파괴"를 구현

=> 데이터를 0으로 만들기

2. 2차원 배열을 1차원 배열로 변환하는 로직을 구현

=> 처음에 상어의 위치를 0으로 가정하고

좌 1, 하 1, 우 2, 상 2, 좌 3, 하 3, 우 4, 상 4, ...

'좌 하 우 상의 순서대로 2개씩 1부터 하나씩 증가' 하는 규칙

but, 그냥 단순하게 visited배열로도 해결 가능

3. 1차원 배열에서 빈 공간을 제거하는 로직을 구현

=>

0이 이면 그냥 넘어가고, 0이 아닌 정수의 값이라면, 배열에 그대로 복사

4. 1차원 배열에서 연속된 숫자가 4개 이상 되는 구슬을 제거하는 로직 구현(구슬을 제거하면서 점수를 계산) ("폭발")

=>
버블 소트를 하는 것처럼, 배열의 시작값 부터 2개씩 비교하면서, 앞선 값과 똑같다면 cnt값을 증가

cnt 값이 4개 이상이 되면서, 다시 다른 숫자가 나와 1로 바뀌는 순간, cnt 값만큼 다시 뒤로 가면서

0으로 만들어주면 됨.

5. 게임 룰에 의한 구슬 확장 구현(A, B)
=> (A :  그룹에 들어있는 구슬의 개서, B : 그룹을 이루고 있는 구슬의 번호 )

1차원 배열에서 하는 것이 맞음.

6. 1차원 배열을 2차원 배열로 변화하는 로직을 구현

=> (2) 의 반대로. 조립은 분해의 역순

'''



#델타 배열 볼줄도 모르네.. 진짜 너 혼나 볼래?!
# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

#처음 0은 무시, 1 : 상, 2 : 하,3 : 좌, 4 : 우
#입력으로 들어오는 값과 위의 델타배열을 mapping
blizard_dir = [0, 0, 2, 1, 3]


#1. 입력에 의한 구슬 파과 구현
def blizard(d, s):
    global ans
    dir = blizard_dir[d]
    #상어는 항상 중앙에
    now_row = (N + 1) // 2 - 1
    now_col = (N + 1) // 2 - 1

    #거리만큼 0으로 바꾸기 => 거리는 반복횟수라 봐도 무방
    for _ in range(s):
        now_row += dr[dir]
        now_col += dc[dir]
        MAP[now_row][now_col] = 0

    lst = matrix_to_list()
    list_to_matrix(remove_zero(lst))

#2. 2차원 배열을 1차원 배열로 변환

def matrix_to_list():

    now_row = (N + 1) // 2 - 1
    now_col = (N + 1) // 2 - 1
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[now_row][now_col] = True
    now_dir = 0
    res = []

    #(0, 0) x, 나선형
    while now_row != 0 or now_col != 0 :
        new_row = now_row + dr[(now_dir + 1) % 4]
        new_col = now_col + dc[(now_dir + 1) % 4]

        #이미 간 곳 이라면, 방향을 바꾸지 않고 그대로 간다.
        if visited[new_row][new_col]:
            now_row = now_row + dr[now_dir]
            now_col = now_col + dc[now_dir]

        #가보지 않은 곳은 방향을 바꾼다.
        else:
            now_row = new_row
            now_col = new_col
            now_dir = (now_dir + 1) % 4
        #나선형 모양으로 데이터들을 리스트에 넣는다
        res.append(MAP[now_row][now_col])
        visited[now_row][now_col] = True

    return res


#3. 1차원 배열에서 빈공간(0)을 제거하는 로직
def remove_zero(lst):

    new_lst = []

    for num in lst:
        #num이 0이 아니면
        if num != 0:
            new_lst.append(num)
    # 나머지 숫자 값을 다 넣고, 폭발로 사라진 빈공간이 아니라, 원래 부터 빈공간이었던 공간도 처리
    # 전체공간에서, 새로 채운 부분을 뺴면 원래부터 빈공간
    new_lst += [0] * ((N ** 2 - 1) - len(new_lst))
    return new_lst


#4. 1차원 배열에서 연속된 숫자가 4개 이상 되는 구슬을 제거하는 로직 구현(구슬을 제거하면서 점수를 계산) ("폭발")
# 굳이 flag가 없어도 될꺼 같은데?
def explode():

    global ans
    flag = True
    while flag:
        flag = False
        lst = matrix_to_list()
        before_num = 0 #구슬 번호 초기화
        num_cnt = 0 #구슬 갯수 초기화

        for i in range(len(lst)):
            target_num = lst[i]

            #둘의 번호가 달라져?!
            if before_num != target_num:
                if num_cnt >= 4:
                    flag = True
                    #점수 계산을 여기서
                    ans += num_cnt * before_num
                    #번호 바뀌기 전 인덱스 부터 cnt 만큼 0으로
                    #슬라이싱으로 범위 넓게 잡아서 값 변경이 가능 => 그 값의 범위만큼 값을 대체
                    lst[i - num_cnt : i] = [0] * num_cnt
                #타켓이 되던것이 이제는 이전 번호가 된다
                before_num = target_num
                num_cnt = 1

            else:
                num_cnt += 1

        list_to_matrix(remove_zero(lst))

#5. 게임 룰에 의한 구슬 확장 구현(A, B)
def expansion():
    lst = matrix_to_list()
    before_num = lst[0]
    num_cnt = 1
    new_lst = []

    for i in range(1, len(lst)):
        target_num = lst[i]
        if before_num != target_num:
            new_lst += [num_cnt, before_num]
            before_num = target_num
            num_cnt = 1

        else:
            num_cnt += 1
    # 범위를 벗어나는건 x, 그래서 new_lst[:N**2 - 1] 슬라이싱으로 제한을 검.
    list_to_matrix(remove_zero(new_lst[:N**2 - 1]))

#6. 1차원 배열을 2차원 배열로 변화 하는 로직
def list_to_matrix(lst):

    now_row = (N + 1) // 2 - 1
    now_col = (N + 1) // 2 - 1

    visited = [[False for _ in range(N)]for _ in range(N)]
    visited[now_row][now_col] = True
    now_dir = 0
    cnt = 0

    while now_row != 0 or now_col != 0 :

        new_row = now_row + dr[(now_dir + 1) % 4]
        new_col = now_col + dc[(now_dir + 1) % 4]

        if visited[new_row][new_col]:

            now_row = now_row + dr[now_dir]
            now_col = now_col + dc[now_dir]

        else:
            now_row = new_row
            now_col = new_col
            now_dir = (now_dir + 1) % 4

        #나선형 찍기, lst에 있는 값 순서대로
        MAP[now_row][now_col] = lst[cnt]
        visited[now_row][now_col] = True
        cnt += 1



N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for _ in range(M):
    d, s = map(int, input().split())
    blizard(d, s)
    explode()
    expansion()

print(ans)

# lst = [1,2,3,4]
# # lst[0:3] = [0] * 4
#
# print(lst[:3])
