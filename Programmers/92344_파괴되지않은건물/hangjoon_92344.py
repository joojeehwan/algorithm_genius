# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/


def solution(board, skills):
    n, m = len(board), len(board[0])
    cs = [[0] * (m + 1) for _ in range(n + 1)]  # 누적합 배열
    for tp, r1, c1, r2, c2, degree in skills:
        if tp == 1:  # 적 공격
            degree *= -1
        # 배치
        cs[r1][c1] += degree
        cs[r2 + 1][c2 + 1] += degree
        cs[r1][c2 + 1] -= degree
        cs[r2 + 1][c1] -= degree

    # 누적합 (위에서 아래)
    for c in range(m + 1):
        for r in range(n):
            cs[r + 1][c] += cs[r][c]

    # 누적합 (왼에서 오른)
    for r in range(n + 1):
        for c in range(m):
            cs[r][c + 1] += cs[r][c]

    # 기존 배열(board)과 합치기
    answer = 0
    for r in range(n):
        for c in range(m):
            board[r][c] += cs[r][c]
            if board[r][c] >= 1:  # 파괴되지 않음
                answer += 1
    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))