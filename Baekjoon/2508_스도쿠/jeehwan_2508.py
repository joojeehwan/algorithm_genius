


# 1. 빈 공간의 좌표만 따로 모으자
# 2. 0인곳을 기준으로 가로 check, 세로 check, 사각형 check => 내가 넣을려는 숫자가 이미 있는지! 그것을 검사 해야함!
# 3. 비어 있는 곳에 1 ~ 9까지의 숫자를 넣어보고!
# 4. 진행하다가 check 했을때, 값이 안 이루어지면! 다시 돌아가서 다른 값을 넣어봐야함 (백트래킹 => dfs 부분)


import sys


input = sys.stdin.readline


MAP = [list(map(int, input().split())) for _ in range(9)]
blank = []


#빈 공간의 좌표만 따로 모으자
for i in range(9):
    for j in range(9):
        if MAP[i][j] == 0:
            blank.append((i, j))

# print(MAP)
# print(*blank)

#가로 체크
def garo_check(row, target):

    for i in range(9):
        if MAP[row][i] == target:
            return False

    return True


#세로 체크
def sero_check(col, target):

    for i in range(9):
        if MAP[i][col] == target:
            return False

    return True

#사각형 체크 => 이렇게 하는 구만,,하하,,
def square_check(row, col, target):

    checking_row = row // 3 * 3
    checking_col = col // 3 * 3
    #각 좌표마다의 좌상단의 사각형 시작지점으로 가서! 작은 사각형을 for문 돌면서 검사한다.
    for i in range(3):
        for j in range(3):
            if target == MAP[checking_row + i][checking_col + j]:
                return False
    return True

#dfs를 돌려보자!!
flag = False
def dfs(lev):
    global flag

    #이미 다 완성을 했는데 다시 뒤로 돌아가면서 check하는 것을 막기 위해서!
    #dfs를 전체 다 돌리는게 아니라 완성하면 이제 더이상 탐색x
    if flag:
        return

    #빈칸의 갯수만큼 lev가 들어가서 다 채웠으면?! -> dfs 끝!
    if lev == len(blank):
        for lst in MAP:
            print(*lst)

        # exit(0)
        flag = True
        return




    #갈 수 있는 숫자의 경우의 수
    for target_number in range(1, 10):
        #빈 공간의 좌표를 가져온다! 이제 lev를 증가시면서 dfs 돌면서 아니면 다시 돌아올꺼다!
        now_row = blank[lev][0]
        now_col = blank[lev][1]

        #싹다 검사해서 통과되면!
        if garo_check(now_row, target_number) and sero_check(now_col, target_number) and square_check(now_row, now_col, target_number):
            MAP[now_row][now_col] = target_number
            #그 다음 숫자 보러 가보자~
            dfs(lev + 1)
            #다시 돌아왔을떄, 숫자를 다시 0으로 비워두기
            MAP[now_row][now_col] = 0

dfs(0)



'''
sudoku = [list(map(int, input().split())) for _ in range(9)]
#해결해야될 칸만 받음
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def is_promising(i, j):
    promising = [1,2,3,4,5,6,7,8,9]  
    
    #행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])
            
    #3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    
    return promising

flag = False #답이 출력되었는가?
def dfs(x):
    global flag
    
    if flag: #이미 답이 출력된 경우
        return
        
    if x == len(zeros): #마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zeros[x]
        promising = is_promising(i, j) #유망한 숫자들을 받음
        
        for num in promising:
            sudoku[i][j] = num #유망한 숫자 중 하나를 넣어줌
            dfs(x + 1) #다음 0으로 넘어감
            sudoku[i][j] = 0 #초기화 (정답이 없을 경우를 대비)
dfs(0)



'''

#갓세진 풀이

'''

우상좌하 대각선의 row, col의 인덱스끼리 더하면 항상 같은 값이 나오는 성질 이용
좌상우하 대각선으 row, col의 인덱스끼리 빼면 항상 같은 값이 나오는 성질 이용


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