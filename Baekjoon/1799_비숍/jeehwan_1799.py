'''

비숍

https://yanoo.tistory.com/47
이해 도움

1. 체스판의 흑백을 이용
color 2차원 배열 만들기
False => 흰칸
True => 검은칸
비숍의 특성상 흰칸에 있는 비숍은 검은칸에 있는 비숍에 영향을 주지 않는다.
효율성을 위해서 나눈다.



2. 갓 세진 풀이 응용

'''


#갓세진 풀이

'''

우상좌하 대각선의 row, col의 인덱스끼리 더하면 항상 같은 값이 나오는 성질 이용
좌상우하 대각선의 row, col의 인덱스끼리 빼면 항상 같은 값이 나오는 성질 이용


체스판에서 나올수 있는 대각선의 가짓수는 2 * n - 1 직접 대각선으로 몇개 나오는지 체크! 

그 나올 수 있는 대각선을 일차원 배열로 생각 index는 몇번쨰 대각선인지, 그 안의 값은 그 대각선에 값이 하나라도 있고 없고를 나타냄! 

같은 대각선상에 있는 것은 위의 2가지 성질에 의해서 인덱스를 뺴거나 더하면 규칙이 나옴! 이것을 이용함! 

'''
#N_Queen

# def dfs(now):
#
#     #now번쨰 줄에 말을 배치한다.
#
#     if now >= N:
#         #맨 끝줄까지 말을 배치 했다.
#         #가지치기를 모두 통과하여 "정상적인 상태이다"
#         global ans
#         ans += 1
#         return
#
#     for col in range(N):
#         if check_col[col]: # 이 열은 앞에서 사용 중이다.
#             continue
#
#         if check_ru_ld[now + col]: # 이 대각선은 앞에서 사용 중이다.
#             continue
#
#         if check_lu_rd[now - col]:
#             continue
#
#         check_col[col] = True
#         check_ru_ld[now + col] = True
#         check_lu_rd[now - col] = True
#
#         MAP[now][col] = 1
#         dfs(now + 1)
#         # 다음 줄로 넘어가라!
#
#         MAP[now][col] = 0
#         #col위치에 두는 방법은 다 해봣으니 기록을 삭제
#
#         check_col[col] = False
#         check_ru_ld[now + col] = False
#         check_lu_rd[now - col] = False
#
#
#
# N = int(input())
#
# check_col = [False] * N
#
# check_ru_ld = [False] * (2 * N -1) # 어떤 대각선(오른쪽 위 ->왼쪽 아래)를 사용했는가?
#
# check_lu_rd = [False] * (2 * N - 1)
#
# ans = 0
#
# MAP = [[0] * N for _ in range(N)]
#
# dfs(0)
#
# print(ans)

n = int(input())


MAP = []
BLACK = []
WHITE = []
COLOR = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        #검은색 칸 표시
        #앞에가 참이면
        # print(i % 2 == 0 and j % 2 == 0)
        # print(i % 2 != 0 and j % 2 != 0)
        #뒤에 굳이 i % 2 != 0 and j % 2 != 0 는 아무거나 적어도 된다.
        COLOR[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)


#print(COLOR)
for row in range(n):
    # row 하나 찍고 -> 한줄 삽잎 -> 그 삽입 col로 체크
    MAP.append(list(map(int, input().split())))
    for col in range(n):
        #비숍이 놓을 수 있는 자리이고, 검은색이면, 좌표 기억하기
        if MAP[row][col] == 1 and COLOR[row][col] == 1:
            BLACK.append((row, col))

        if MAP[row][col] == 1 and COLOR[row][col] == 0:
            WHITE.append((row, col))

print(BLACK, WHITE)
#검은색인 경우
bcnt = 0
#하얀색인 경우
wcnt = 0

check_ld_ru = [0] * (2*n - 1)
check_lu_rd = [0] * (2*n - 1)

def dfs(EachChessMap, lev, count):

    global bcnt, wcnt

    if lev == len(EachChessMap):
        end_row, end_col = EachChessMap[lev - 1]
        if COLOR[end_row][end_col]:
            bcnt = max(bcnt, count)
        else:
            wcnt = max(wcnt, count)

        return

    now_row, now_col = EachChessMap[lev]
    #now_row - now_col + n + 1 를 하는 이유?! 음수 제거
    # 이곳은 그냥 건너 뛰어라! 비숍이 놓일 수 없다.
    if check_ld_ru[now_row + now_col] or check_lu_rd[now_row - now_col + n - 1] :
        dfs(EachChessMap, lev + 1, count)

    # 비숍이 놓일 수 있다.
    else:
        #비숍이 놓이니 기록을 하자
        check_ld_ru[now_row + now_col] = 1
        check_ld_ru[now_row  - now_col + n - 1] = 1
        dfs(EachChessMap, lev + 1, count + 1)
        #한번 간곳도, 다시 돌아와서 아닌 곳도 탐색해봐야 하니! 백트래킹을 위한 코드 부분
        # 한 번 간곳을 제거하는 부분
        check_ld_ru[now_row + now_col] = 0
        check_ld_ru[now_row - now_col + n - 1] = 0
        dfs(EachChessMap, lev + 1, count)

# 검은색이나, 흰색의 체스말이 존재하면, 돌려라! 무한히 반복 되는 것이 아님
# 길이가 하나라도 있으면, 진행 되고, 안에서 dfs 돌리고, 연산 끝나면, 다음
# 다른 색깔의 체스말을 체크 하는 것.
if len(BLACK) > 0 :
    dfs(BLACK, 0, 0)

if len(WHITE) > 0 :
    dfs(WHITE, 0, 0)

print(bcnt + wcnt)