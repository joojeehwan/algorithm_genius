# 누적합 이용

def solution(board, skill):

    n = len(board)
    m = len(board[0])

    MAP = [[0] * (m+1) for _ in range(n+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            MAP[r1][c1] -= degree
            MAP[r1][c2 + 1] += degree
            MAP[r2 + 1][c1] += degree
            MAP[r2 + 1][c2 + 1] -= degree
        else:
            MAP[r1][c1] += degree
            MAP[r1][c2 + 1] -= degree
            MAP[r2 + 1][c1] -= degree
            MAP[r2 + 1][c2 + 1] += degree

    # 가로 < 세로 순서로 누적합을 만들어준다
    for i in range(n):
        for j in range(1, m):
            MAP[i][j] += MAP[i][j-1]

    for j in range(m):
        for i in range(1, n):
            MAP[i][j] += MAP[i-1][j]

    answer = 0

    # 파괴되지 않은 건물 세기
    for i in range(n):
        for j in range(m):
            if MAP[i][j] + board[i][j] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))

