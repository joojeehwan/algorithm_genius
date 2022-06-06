"""
괄호를 도대체 어떻게 해야할지 감이 안잡혀서
괄호를 넣은 식을 리스트로 만들어야하나 생각했지만
정답은 dp[4] = (dp[1]&dp[3], dp[2]&dp[2], dp[3]&dp[1]) 이런식으로 만드는 것이었다. (그냥 연산한다는 뜻에서 &를 씀..)
우선 dp[1]&dp[3] 과 dp[3]&dp[1] 처럼 순서를 바꿔야 하는 이유는 빼기와 나눗셈 때문이다.
쉬운 예를 위해 dp[1]&dp[2] 와 dp[2]&dp[1]로 설명을 해보자면,
dp[1] = {5}, dp[2] = {10, 0, 25, 1, 55}일 때
dp[2]&dp[1]만 하면 1-5 에서 -4가 나온다.(5/5-5)
하지만 (5-5/5)로 4도 나올 수 있는데 나오지 않게된다. 이러한 점에서 순서를 뒤집는 경우가 필요하다.
그리고 다시 dp[4]에서 dp[2]&dp[2]가 필요한 이유는 괄호 때문이다.
(N&N) & (N&N)처럼 괄호를 직접적으로 쓰지 않지만 괄호를 쓴 것 처럼 계산하는 것이다.
eunchan-Kang 의 python 정답 & 설명을 봤음
"""
def solution(N, number):
    answer = -1
    if N == number:
        return 1

    # N을 i개 써서 만들어낸 숫자들
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for idx_dp in range(2, 9):
        new_result = [int(str(N)*idx_dp)]
        idx = 1
        while idx < idx_dp:
            first_bracket = dp[idx]
            second_bracket = dp[idx_dp-idx]

            for first in first_bracket:
                for second in second_bracket:
                    new_result += [first+second, first-second, first*second]
                    if second != 0:
                        new_result.append(int(first/second))
            idx += 1

        if number in new_result:
            answer = idx_dp
            break

        dp[idx_dp] = set(new_result)

    return answer

print(solution(7, 91))
