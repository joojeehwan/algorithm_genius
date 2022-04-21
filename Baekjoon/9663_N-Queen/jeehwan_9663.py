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