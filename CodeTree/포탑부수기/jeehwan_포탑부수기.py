'''



1. 행과 열 순서 -> 열 순서

 행과 열의 합이 가장 큰?!

=> n - queen 에서의 문제 테크닉

격자에서, 같은 대각선에 있는 것들은
row + col의 합이 같다.

이를 통해 순회를 하면, 자연스럽게 (행 + 열) 큰 순서 -> (열) 큰 순서로 순회


추가) 1. 정렬로 풀어도 됨.

     2. 아니면 자료구조를 처음에 저장 => 데이터 낭비?





2. 격자 밖으로 이동하면, 연결되는 격자

=> 모듈러

아 그떄, 하은이가 물어봤던 부분,

 ( now_row + dr[i] + n) % n

 여기서 n 을 굳이 더하는 이유는?!

 python의 경우는  -1 % 4  = 3 으로 잘 계산 하는데,

 다른 언어에서는 -1 % 4를 -1 로 할 수 도 있다.

 => 음수에 대한 나머지 연산은, ub라고 한다.


 즉, ub(unexpectd behavior), 언어에 따라 값이 다르게 나온다.




3. 공격대상 선정시 "우 하 좌 상"의 우선선위로 경로를 선택

=> dr / dc를 초기부터 문제에 주어진 대로 설정




4. bfs의 최단경로구하는 skill

 => "역추적 "



'''
lst = [3, 2, 1]
lst.sort()
print(lst)
from collections import deque

# 류호석 풀이 + 시험장에서의 내 풀이

#초기 입력
N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

#해당 턴에 공격과 관련 여부 check
#isAttacked = [[False for _ in range(M)] for _ in range(N)]
#마지막으로 공격언제 했니?!
lastAttackCnt = [[0 for _ in range(M)] for _ in range(N)]
# 단순히 해당 격자에 값을 뺴, "공격"을 구현하는 함수
# 해당 함수 실행시, 공격과 연관을 기록해, 마자막 정비에서 활용

#"상 하 좌 우"의 순서대로 델타 배열 설정

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def attack(row, col, power):
    isAttacked[row][col] = True
    return max(0, MAP[row][col] - power)

#부서지지 않은 포탑이 1개가 된다면, 그 즉시 시물레이션을 종료
def isFinish():

    cnt = 0
    for row in range(N):
        for col in range(M):
            if MAP[row][col] > 0 :
               cnt += 1

    if cnt == 1:
        return True

    else:
        return False


# 이 부분에서 내가 했던 풀이 적용해보기
# 갑자기 시험장에서 내가 n - queen 풀었던게 생각나서 풀 수 있는 확률은?!
# 제로에 가깝다.
# bfs에서 "역추적 알고리즘" 같은거를 생각하는데 더 집중해야 해.

def select_attacker_jeehwan():

    #정렬로 구현해보기
    candidate = []
    for row in range(N):
        for col in range(M):
            if MAP[row][col] :
                candidate.append((row, col, MAP[row][col], lastAttackCnt[row][col], row+col, col))

    candidate.sort(key = lambda x : (x[2], -x[3], -x[4], -x[5]))
    return candidate[0][0] , candidate[0][1]


def select_attacker_hoseok():

    minValue, maxTime, minRow, minCol = 1e9, -1, 0, 0

    for sum in range(N + M - 2, -1, -1) :  # SUM(행 + 열)을 최대부터, 최소까지 순회
        for col in range(M - 1, -1, -1) :  # 같은 SUM에 대해서는, 높은 열부터 탐색

            row = sum - col

            if row < 0 or row >= N:
                continue

            if MAP[row][col] == 0:
                continue

            if minValue > MAP[row][col] :
                minValue, maxTime, minRow, minCol = MAP[row][col], lastAttackCnt[row][col], row, col

            elif minValue == MAP[row][col] and maxTime < lastAttackCnt[row][col]:
                minValue, maxTime, minRow, minCol = MAP[row][col], lastAttackCnt[row][col], row, col

    return minRow, minCol


def select_target():
    maxValue, minTime, maxRow, maxCol = -1, 1e9, 0, 0

    for sum in range(N + M - 2, -1, -1):  # SUM(행 + 열)을 최대부터, 최소까지 순회
        for col in range(M - 1, -1, -1):  # 같은 SUM에 대해서는, 높은 열부터 탐색

            row = sum - col

            # 이걸 왜 하지?!
            # row 가 sum - col이라서
            if row < 0 or row >= N:
                continue

            if MAP[row][col] == 0:
                continue

            if maxValue < MAP[row][col]:
                maxValue, minTime, maxRow, maxCol = MAP[row][col], lastAttackCnt[row][col], row, col

            elif maxValue == MAP[row][col] and minTime > lastAttackCnt[row][col]:
                maxValue, minTime, maxRow, maxCol = MAP[row][col], lastAttackCnt[row][col], row, col

    return maxRow, maxCol


#여기가 문제의 그 부분,,,!
def tryRaser(attacker, target):

    visited = [[False for _ in range(M)]for _ in range(N)]

    backTracking = [[None for _ in range(M)] for _ in range(N)]

    q = deque()
    q.append(attacker)
    visited[attacker[0]][attacker[1]] = True

    while q :
        now_row, now_col = q.popleft()

        for k in range(4) :

            #모듈려 연산
            next_row = (now_row + dr[k] + N) % N
            next_col = (now_col + dc[k] + M ) % M

            # 범위 생각?! 여기선 할 필요 없다..!
            # 범위 밖이라는 것이 존재하지 않아

            # 이미 간곳도 가지 않아.
            if visited[next_row][next_col] :
                continue

            # 부서진 포탑이 있는 곳은 갈 수 없다.
            if MAP[next_row][next_col] == 0:
                continue

            #(next_row, next_col)은 (now_row, now_col)에서 왔다.
            backTracking[next_row][next_col] = (now_row, now_col)
            visited[next_row][next_col] = True
            q.append((next_row, next_col))

    # 결국 타켓까지 가지 못하는 경우
    # 이어져 있는 포탑의 경로가 없는 경우
    if not visited[target[0]][target[1]]:
        return False


    # 레이저가 도달할 수 있는 경우?!
    # 백 트래킹 돌면서, 가는 경로에 있는 포탑들의 공격력 낮추기
    row, col = target

    while row != attacker[0] or col != attacker[1] :
        power = MAP[attacker[0]][attacker[1]] // 2

        #공격이 대상은 //2 안하고 공격
        if row == target[0] and col == target[1] :
            power = MAP[attacker[0]][attacker[1]]

        MAP[row][col] = attack(row, col, power)
        # 아래 코드를 통해서, 현재의 row, col에 오기 위해 왔던
        # 이전 (row, col)를 찾아갈 수 있음.
        row, col = backTracking[row][col]


# 8방향의 dr / dc 를 만들어도 되지만!
# 이중for문을 활용해 (-1, 0, 1) 를 통해서도 구현 가능

def bomb(attacker, target):

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):

            next_row = (target[0] + dr + N) % N
            next_col = (target[1] + dc + M) % M

            #공격자는 해당 공격에 영향을 받지 않음.
            if next_row == attacker[0] and next_col == attacker[1] :
                continue

            power = MAP[attacker[0]][attacker[1]] // 2
            if next_row == target[0] and next_col == target[1] :
                power = MAP[attacker[0]][attacker[1]]

            MAP[next_row][next_col] = attack(next_row, next_col, power)


def improve():
    for row in range(N):
        for col in range(M):
            if isAttacked[row][col] :
                continue

            if MAP[row][col] == 0:
                continue

            MAP[row][col] += 1



# 전체 시물레이션 진행


for tm in range(1, K + 1):

    if isFinish(): #만약 종료 조건을 만족!? 턴을 수행하지 않고, 종료
        break

    # 공격자, 타켓 선정

    attacker = select_attacker_hoseok()
    target = select_target()

    #공격자의 공격력을 증가 시킴



    #공격자에 대해서, 공격턴을 기록,
    lastAttackCnt[attacker[0]][attacker[1]] = tm
    isAttacked = [[False for _ in range(M)] for _ in range(N)]
    isAttacked[attack([0])][attacker[1]] = True


    if not tryRaser(attacker, target):
        bomb(attacker, target)


    #6. 정비
    improve()

#모든 과정이 끝나고, 가장 강한 녀석


res = select_target()
print(MAP[res[0]][res[1]])







