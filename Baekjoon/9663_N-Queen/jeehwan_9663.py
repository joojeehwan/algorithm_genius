#풀이가 2가지 있는 듯,,!
#1. 한꺼번에 같이 열을 같이 확인

'''

퀸은 놓지 못하는 경우 2가지

1. 같은 열에 있는 경우

row[i] = j  == 퀸의 위치가 [i, j]라고 있는것!

so row[i] = j에서 i가 변화할때마다 j가 같은 값이 있는 지 확인하면 된다.


2. 왼쪽, 오른쪽 대각선에 다른 퀸이 있는 경우

맨위에서부터 한칸식 내려가면서 퀸을 놓고 있기 때문에

좌상 대각선, 우상대각선만 확인하면 됨.

사각행렬의 특성상, 대각선상에 있는 두 좌표 사이에는

|x1 - x2| == |y1 - y2| 가 성립한다!

ex)
만약에 현재 퀸을 놓은 위치가 (3, 3)라고 가정하면, 왼쪽 대각선의 좌표는 각각 (2, 2), (1, 1), (0, 0)이 된다.

여기서, (3, 3)을 i와 j라고 하고, (2, 2)를 x1, y1, (1, 1)을 x2, y2, (0, 0)을 x3, y3이라고 해보자.

i에서 x1을 뺀 값과 j에서 y1를 뺀 값은 모두 1로 같다.

또한, i에서 x2를 뺀 값과 j에서 y2를 뺀 값은 모두 2로 같다.

세 번째 경우도 3으로 마찬가지로 동일하다.

두 번째로, 오른쪽 위 대각선 값들을 살펴보자.

동일하게 현재 퀸의 위치가 (3, 3)이라고 가정하면 오른쪽 대각선의 좌표는 (2, 4), (1, 5), (0, 6)이 된다.

마찬가지로 (3, 3)을 i, j로, (2, 4)를 x1, y1, (1, 5)를 x2, y2, (0, 6)을 x3, y3로 두고 i, j값에서 x와 y를 뺀 값을 살펴보면

(1, -1), (2, -2), (3, -3)이 된다.

'''

N = int(input())

ans = 0
row = [0] * N


def isPossible(row_point):

    for col_point in range(row_point):
        #열 / 대각선상 check
        if row[row_point] == row[col_point] or row_point - col_point == abs(row[row_point] - row[col_point]):
            return False
    return True


def dfs(lev):

    global ans

    #맨 위에서 부터 맨아래의 행까지 퀸을 다 놓았다.
    if lev == N:
        ans += 1
        return

    else:
        #행에서 몇번쨰에 놓일 수 있냐?! COL
        for next_col in range(N):
            # [lev, next_col]에 퀸이 위치
            row[lev] = next_col
            if isPossible(lev):
                dfs(lev + 1)

dfs(0)
print(ans)

#2. 열을 따로 두고, 열을 check하는 배열을 하나 더 두는 행위
'''
import sys 
N = int(sys.stdin.readline()) 
row = [0] * N 
cnt = 0 
visit = [False] * N 

# Queen이 서로 공격할 수 없는 지 확인 

def check(q): 
    for i in range(q): 
        if abs(row[q] - row[i]) == q - i: # 대각선에 Queen이 있는지 확인 
        return False 
    return True 
    
# DFS로 방법으로 탐색 
def dfs(q): 
    global cnt 
    
    if q == N: 
        cnt += 1 
        return 
    for i in range(N): 
        if visit[i]: # 같은 열에 Queen이 있는가 
            continue 
            
    row[q] = i 
    if check(q): 
        visit[i] = True 
        dfs(q + 1) 
        visit[i] = False 
        
dfs(0) 
print(cnt)

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

def dfs(now):

    #now번쨰 줄에 말을 배치한다.

    if now >= N:
        #맨 끝줄까지 말을 배치 했다.
        #가지치기를 모두 통과하여 "정상적인 상태이다"
        global ans
        ans += 1
        return

    for col in range(N):
        if check_col[col]: # 이 열은 앞에서 사용 중이다.
            continue

        if check_ru_ld[now + col]: # 이 대각선은 앞에서 사용 중이다.
            continue

        if check_lu_rd[now - col]:
            continue

        check_col[col] = True
        check_ru_ld[now + col] = True
        check_lu_rd[now - col] = True

        MAP[now][col] = 1
        dfs(now + 1)
        # 다음 줄로 넘어가라!

        MAP[now][col] = 0
        #col위치에 두는 방법은 다 해봣으니 기록을 삭제

        check_col[col] = False
        check_ru_ld[now + col] = False
        check_lu_rd[now - col] = False



N = int(input())

check_col = [False] * N

check_ru_ld = [False] * (2 * N -1) # 어떤 대각선(오른쪽 위 ->왼쪽 아래)를 사용했는가?

check_lu_rd = [False] * (2 * N - 1)

ans = 0

MAP = [[0] * N for _ in range(N)]

dfs(0)

print(ans)