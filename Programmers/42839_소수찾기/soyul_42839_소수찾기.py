# 소수인지 확인하는 함수
def check(num):

    if num <= 1:
        return False
    if num == 2:
        return True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):

    nums = set()

    # 모든 숫자 조합을 만들어줌
    def dfs(numbers, n, num, used):

        if len(num) >= n:
            nums.add(int(num))
            return

        for i in range(len(numbers)):
            if used[i]:
                continue

            used[i] = 1
            dfs(numbers, n, num + numbers[i], used)
            used[i] = 0

    for i in range(1, len(numbers)+1):
        used = [0] * len(numbers)
        numbers = sorted(numbers)
        dfs(numbers, i, '', used)

    answer = 0
    for num in nums:
        answer += check(num)
    return answer