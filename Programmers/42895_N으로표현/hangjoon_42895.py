# https://haesoo9410.tistory.com/270


def solution(N, number):
    dp = [set() for _ in range(9)]  # N을 1 ~ 8개 사용하여 만들어 낼 수 있는 경우의 수(중복 x)

    for cnt in range(1, 9):
        # N 으로만 구성된 수
        dp[cnt].add(int(str(N) * cnt))

        # 사칙연산으로 만드는 수
        for i in range(cnt // 2 + 1):  # cnt 의 절반만 순회하면 모든 경우의 수 탐색가능
            # op1 와 op2를 합치면(더하기 x) (cnt)개의 N으로 만들 수 있는 수가 나옴
            for op1 in dp[i]:
                for op2 in dp[cnt - i]:
                    # 더하기
                    dp[cnt].add(op1 + op2)
                    # 빼기
                    if op1 - op2 > 0:
                        dp[cnt].add(op1 - op2)
                    if op2 - op1 > 0:
                        dp[cnt].add(op2 - op1)
                    # 곱하기
                    dp[cnt].add(op1 * op2)
                    # 나누기
                    if op1 and op2 // op1:
                        dp[cnt].add(op2 // op1)
                    if op2 and op1 // op2:
                        dp[cnt].add(op1 // op2)

        # 내가 원하는 수(number)가 (cnt)개로 만들어질 수 있으면 반환, 작은 값부터 순회하기 때문에 바로 반환 가능
        if number in dp[cnt]:
            return cnt

    # 1 ~ 8 개의 N 으로는 만들어질 수 없음
    return -1


print(solution(5, 12))
print(solution(2, 11))
print(solution(5, 26))
print(solution(8, 5800))
print(solution(1, 1121))
print(solution(2, 31168))