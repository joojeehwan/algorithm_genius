"""
1. 1 ~ 4 분면으로 어딘지 파악한다.
2. 계속 들어간다. 범위의 길이가 1이 될 때 까지
3. 내 앞에 몇개가 있느냐...
3-0. 한 변의 길이는 2 ** N 이다.
3-1. 내가 1분면이다. 그렇다면 내 앞에 없다.
3-2. 내가 2분면이다. 그렇다면 4 ** (n-1) 개가 내 앞에 있다. (2^(N-1) * 2^(N-1))
3-3. 내가 3분면이다. 그렇다면 2 * (4 ** (n-1)) 개가 내 앞에 있다.
3-4. 내가 4분면이다. 그렇다면 3 * (4 ** (n-1)) 개가 내 앞에 있다.
"""

N, goal_row, goal_col = map(int, input().split())
answer = 0


def divide_conquer(n, row, col):
    global answer
    if row == goal_row and col == goal_col:
        return
    # 일단 N을 하나 줄인다.
    n -= 1
    # 4분면을 사용하므로 반의 길이를 구한다.
    half_width = 2 ** n

    # 1,2,3,4분면 중 어떤 곳인지 확인하기 위한 Flag 변수
    row_over = True if goal_row >= row + half_width else False
    col_over = True if goal_col >= col + half_width else False

    # 한 분면당 가진 칸의 수
    block_cnt = 4 ** n

    if not row_over:
        if not col_over:
            # 1사분면
            divide_conquer(n, row, col)
        else:
            # 2사분면
            answer += block_cnt
            divide_conquer(n, row, col+half_width)
    else:
        if not col_over:
            # 3사분면
            answer += 2 * block_cnt
            divide_conquer(n, row+half_width, col)
        else:
            # 4사분면
            answer += 3 * block_cnt
            divide_conquer(n, row+half_width, col+half_width)


divide_conquer(N, 0, 0)
print(answer)