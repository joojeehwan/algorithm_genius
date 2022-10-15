'''

참고

https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/#%EB%AC%B8%EC%A0%9C-6-%ED%8C%8C%EA%B4%B4%EB%90%98%EC%A7%80-%EC%95%8A%EC%9D%80-%EA%B1%B4%EB%AC%BC


누적합 문제


2차원 배열에 대한 구간의 변화를 처리하는 방법을 설명드리기 전에, 우선 1차원 배열을 효율적으로 처리할 수 있는 방법을 설명드리겠습니다.

예를 들어, [1,2,4,8,9]의 배열이 있고, 0번째부터 3번째 원소까지 2만큼 빼야 하는 상황이라고 가정하겠습니다.

즉, 배열을 [-1,0,2,6,9]로 만들고 싶은 상황입니다. 가장 쉬운 방법으로는 0번째부터 3번째 원소까지 반복문을 사용해 2만큼 빼주는 방법이 있지만, 이 방법은 O(M)의 시간 복잡도가 걸립니다.

O(M)의 시간 복잡도를 O(1)로 만들 수 있는 방법은 바로 누적합을 이용하는 방법입니다.

위의 예시의 경우 [-2,0,0,0,2]를 저장한 새로운 배열을 생성합니다.

이 배열을 앞에서부터 누적합하면 [-2,-2,-2,-2,0]이 되기 때문에 초기 배열인 [1,2,4,8,9]과 더해주면 [-1,0,2,6,9]를 얻을 수 있게 됩니다.

즉, 1차원 배열의 a번째 원소부터 b번째 원소까지 c만큼의 변화를 주겠다고 하면 새로운 배열의 a번째 원소에 c를 더하고 b+1번째 원소에 c를 빼면 됩니다.

이 방식으로 문제를 풀면 O(N * M * K)의 복잡도를 O(N * K)로 줄일 수 있지만, 이 또한 시간 초과가 발생합니다.

따라서 이 아이디어를 2차원 배열로 확장해 줘야 합니다. 이번엔 2차원 배열에서 (0,0)부터 (2,2)까지 n만큼 변화시키는 경우를 예로 들어보겠습니다.

배열의 행만 따로 봐서 위에서 설명한 아이디어를 하나의 행씩 적용시키면, 1차원 배열의 0번째 원소부터 2번째 원소까지 n만큼의 변화를 3개의 행에 적용시키는 것이 됩니다.

n 0 0 -n
n 0 0 -n
n 0 0 -n
위 행렬을 다시 열만 따로 보면, 가장 왼쪽 열의 0번째 원소부터 2번째 원소까지 n만큼의 변화와 가장 오른쪽 열의 0번째 원소부터 2번째 원소까지 -n만큼의 변화와 같습니다. 각 열에 위의 아이디어를 적용시키면 아래와 같습니다. 이런 식으로 2차원 배열에도 적용시킬 수가 있습니다.

n 0 0 -n
0 0 0 0
0 0 0 0
-n 0 0 n
즉, 2차원 배열에서 (x1,y1)부터 (x2,y2)까지 n만큼의 변화는 (x1,y1)에 +n, (x1,y2+1)에 -n, (x2+1,y1)에 -n, (x2+1,y2+1)에 +n을 한 것과 같습니다. 위 배열을 위에서 아래로 누적합한 뒤, 왼쪽에서 오른쪽으로 누적합하거나 왼쪽에서 오른쪽으로 누적합 한 뒤, 위에서 아래로 누적합하면 처음에 의도한 (0,0)부터 (2,2)까지 n만큼 변화시키는 배열이 나오는 것을 확인할 수 있습니다.

n n n 0
n n n 0
n n n 0
0 0 0 0
이러한 방법으로 skill의 한 원소를 O(1)만에 처리할 수 있다는 것을 알 수 있습니다. 따라서 위의 방법으로 K개의 skill을 모두 처리할 수 있는 배열을 만드는데 O(K)가 걸리게 됩니다. 그리고 해당 배열을 누적합 배열로 바꾸는 과정이 필요한데, 행과 열을 각각 누적합 해줘야 하기 때문에 O(N * M)가 걸리게 됩니다. 따라서 O(K + N * M)으로 문제를 해결할 수 있습니다.

이해를 돕기 위해 2번 테스트케이스를 예시로 추가 설명드리겠습니다.

1. (1,1)부터 (2,2)까지 -4만큼 변화를 줘야 합니다. (배열의 (1,1)과 (3,3)에 -4, 배열의 (1,3)과 (3,1)에 4만큼 변화를 줍니다.)

     0    0    0    0
     0   -4    0    4
     0    0    0    0
     0    4    0   -4
2. (0,0)부터 (1,1)까지 -2만큼 변화를 줘야 합니다. (배열의 (0,0)과 (2,2)에 -2, 배열의 (0,2)과 (2,0)에 2만큼 변화를 줍니다.)

    -2    0    2    0
     0   -4    0    4
     2    0   -2    0
     0    4    0   -4
3. (2,0)부터 (2,0)까지 +100의 변화를 줘야 합니다. (배열의 (2,0)과 (3,1)에 100, 배열의 (2,1)과 (3,0)에 -100만큼 변화를 줍니다.)

    -2    0    2    0
     0   -4    0    4
    102  -100 -2    0
   -100   104  0   -4
이 배열을 이제 위에서 아래로 누적합 해주겠습니다.

-2    0    2    0
-2   -4    2    4
100  -104  0    4
 0    0    0    0
그다음 왼쪽에서 오른쪽으로 누적합 해주겠습니다.

-2   -2    0    0
-2   -6   -4    0
100  -4   -4    0
 0    0    0    0
이 배열을 board와 합쳐 주겠습니다.

1 2 3         -2  -2   0        -1  0  3
4 5 6    +    -2  -6  -4    =    2 -1  2
7 8 9         100 -4  -4        107 4  5
마지막 결과 배열과 같은 배열이 나왔습니다. 이 배열에서 0보다 큰 정수의 개수를 구하면 됩니다.

'''

def solution(board, skill):
    tboard = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for typ, r1, c1, r2, c2, degree in skill:
        tboard[r1][c1]+=(2*typ-3)*degree
        tboard[r2+1][c2+1]+=(2*typ-3)*degree
        tboard[r2+1][c1]-=(2*typ-3)*degree
        tboard[r1][c2+1]-=(2*typ-3)*degree
    #누적합 왼쪽에서 오른쪽
    for i in range(1, len(tboard[0])):
        tboard[0][i]+=tboard[0][i-1]
    #누적합 위에서 아래
    for i in range(1, len(tboard)):
        tboard[i][0]+=tboard[i-1][0]

    for x in range(1, len(tboard)):
        for y in range(1, len(tboard[0])):
            tboard[x][y]+=tboard[x][y-1]+tboard[x-1][y]-tboard[x-1][y-1]
    ans = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y]+tboard[x][y]>0: ans+=1
    return ans




#다른 풀이

def make_prefix_sum(board, skill):  # 누적합을 기록하는 리스트 만드는 부분
    prefix_sum = board
    board_h, board_w = len(board), len(board[0])

    prefix_sum = [[0 for i in range(board_w + 1)] for i in range(board_h + 1)]  # 가로 세로 +1 크기의 리스트
    for item in skill:  # type = 1 : 공격, type = 2 : 회복, -1.5하고 2를 곱하면 +1 이나 -1이 됨.
        prefix_sum[item[1]][item[2]] += (item[0] - 1.5) * 2 * item[5]  # 왼쪽 윗 꼭짓점.
        prefix_sum[item[1]][item[4] + 1] -= (item[0] - 1.5) * 2 * item[5]  # 오른쪽 윗 꼭짓점.
        prefix_sum[item[3] + 1][item[2]] -= (item[0] - 1.5) * 2 * item[5]  # 왼쪽 아래 꼭짓점.
        prefix_sum[item[3] + 1][item[4] + 1] += (item[0] - 1.5) * 2 * item[5]  # 오른쪽 아래 꼭짓점.
    return prefix_sum


def get_prefix_sum(board):  # 누적합 더하는 부분
    prefix_sum = board
    board_h, board_w = len(board), len(board[0])

    for i in range(1, board_h):  # 첫칸은 자기 자신이니까 0이 아닌 1부터 시작했음.
        for j in range(board_w):
            prefix_sum[i][j] += prefix_sum[i - 1][j]  # 위에서 아래 방향으로 누적합
    for i in range(board_h):
        for j in range(1, board_w):
            prefix_sum[i][j] += prefix_sum[i][j - 1]  # 왼쪽에서 오른쪽 방향으로 누적합
    return prefix_sum


def solution(board, skill):
    answer = 0
    board_h, board_w = len(board), len(board[0])
    prefix_sum_list = make_prefix_sum(board, skill)
    prefix_sum = get_prefix_sum(prefix_sum_list)

    for i in range(board_h):
        for j in range(board_w):
            board[i][j] = board[i][j] + prefix_sum[i][j]

    for item in board:
        for j in item:
            if j > 0:
                answer += 1

    return answer
