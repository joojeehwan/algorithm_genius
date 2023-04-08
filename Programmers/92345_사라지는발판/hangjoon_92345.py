# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/
# https://tiktaek.tistory.com/88


def moving(a, b, board, turn=0):
    global m, n
    # 초기값
    if turn % 2:  # b 차례
        r, c = b
    else:  # a 차례
        r, c = a
    flag = 0  # 움직일 수 있는지
    isWin = False
    mini, maxi = 987654321, 0
    # 내 발판이 사라짐 = 패배
    if not board[r][c]:
        return isWin, 0
    # 진행 중
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # 남동북서
        new_r, new_c = r + dr, c + dc
        if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n:  # 맵 밖임
            flag += 1
            continue
        if not board[new_r][new_c]:  # 이미 사라짐
            flag += 1
            continue
        # 이동
        board[r][c] = 0
        # 다음 step
        if turn % 2:  # b 차례 -> a 차례
            result, new_cnt = moving(a, (new_r, new_c), board, turn + 1)
        else:  # a 차례 -> b 차례
            result, new_cnt = moving((new_r, new_c), b, board, turn + 1)
        if not result:  # 상대방이 패배 = 나의 승리 = 최소 이동으로 승리해야 함
            isWin = True
            mini = min(mini, new_cnt)
        else:  # 상대방이 승리 = 나의 패배 = 최대 이동으로 패배해야 함
            maxi = max(maxi, new_cnt)
        # 복구
        board[r][c] = 1
    # 판별
    if flag == 4:  # 움직일 수 없음 = 패배
        return isWin, 0
    if isWin:  # 승리한 경우 최소이동 반환
        return isWin, mini + 1
    else:  # 패배한 경우 최대이동 반환
        return isWin, maxi + 1


def solution(board, aloc, bloc):
    global m, n, answer, res
    m, n = len(board), len(board[0])
    result, answer = moving(aloc, bloc, board)
    return answer


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
print(solution([[1]], [0, 0], [0, 0]))