"""
잘 풀다가 몇몇 엣지 케이스 때문에 헤멘 문제.
1. 역시나 1,000,000,007 나누기 안해주고 틀렸고
2. 런타임 에러는 puddle dp맵에 저장할 때 r, c를 반대로 저장해야하는데 안그래서 틀렸고
3. dp[row][col] = dp[row-1][col] + dp[row][col-1] 은 빨리 찾아냈으나,
    첫 번째 가로줄과 세로줄을 다 1로 저장하고 시작했다가 문제가 생겼다.
    웅덩이가 있으면 1번에 갈 수 없기 때문이다. (1,9,10번이 틀렸던 이유)
[집, 웅덩이, 학교] 와 같은 경우가 있는데 이때 웅덩이 때문에 학교에 갈 수 없다.
근데 1번째 가로줄이라서 다 1로 처리해버리면 갈 수 있다고 표기하게 된다.
이를 해결하자 문제는 풀렸다.

대신 웅덩이를 판가름하는 분기문이 마음에 안든다.
점수 : 1166 (+16)
"""
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]

    # 웅덩이를 표기한다.
    for r, c in puddles:
        dp[c-1][r-1] = -1

    # 첫 번째 가로 줄을 다 1로 채운다.
    for x in range(m):
        # 웅덩이를 한번이라도 만나면 1번에 갈 수 없다.
        if dp[0][x] == -1:
            break
        dp[0][x] = 1

    # 첫 번째 세로 줄을 다 1로 채운다.
    for y in range(n):
        # 웅덩이를 한번이라도 만나면 1번에 갈 수 없다.
        if dp[y][0] == -1:
            break
        dp[y][0] = 1

    for row in range(1, n):  # 첫 번째 가로줄은 볼 필요 X
        for col in range(1, m):  # 첫 번째 세로 줄은 볼 필요 X
            if dp[row][col] == -1:  # 물 웅덩이면 넘어가
                continue
            # 왼쪽, 위쪽 다 웅덩이가 아닌 경우
            if dp[row][col-1] >= 0 and dp[row-1][col] >= 0:
                dp[row][col] = dp[row][col-1] + dp[row-1][col]
            # 왼쪽만 웅덩이인 경우
            elif dp[row][col-1] == -1 and dp[row-1][col] >= 0:
                dp[row][col] = dp[row-1][col]
            # 위쪽만 웅덩이인 경우
            elif dp[row-1][col] == -1 and dp[row][col-1] >= 0:
                dp[row][col] = dp[row][col-1]
            # 둘 다 웅덩이면 갈 수 없다.

    return dp[n-1][m-1] % 1000000007


print(solution(3, 3, [[1,2]]))
