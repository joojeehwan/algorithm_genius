import math
from itertools import permutations


def is_prime_number(n):
    if n == 0 or n == 1:
        return False


    else:
        # 반만 가도 알 수 있고!
        for i in range(2, int(math.sqrt(n)) + 1):
            # 0이 되면 소수가 아니니깐!
            if n % i == 0:
                return False

        return True


def solution(numbers):
    answer = []

    # 조합의 경우의 수를 찾고!
    for i in range(1, len(numbers) + 1):
        lst = list(permutations(numbers, i))
        print(lst)
        # lst의 수만큼 숫자로 바궈서 -> isPrime 검사!
        for j in range(len(lst)):
            num = int("".join(lst[j]))
            print(num)
            if is_prime_number(num):
                answer.append(num)

    # 결국엔 중복제거!
    answer = list(set(answer))

    return len(answer)


import math


# isPrime 함수
def is_Prime(Num):
    if Num == 0 or Num == 1:
        return False

    else:
        for i in range(2, int(math.sqrt(Num)) + 1):
            if Num % i == 0:
                return False

        return True


def dfs(lev, word, max_Len, visited, numbers):
    # 종료 조건
    if lev == max_Len:  # 중복제거
        if word not in numbers:
            if word[0] == "0":
                numbers.append(word[1:])
            else:
                numbers.append(word)
        return

        # dfs
    for i in range(max_Len):
        if not visited[i]:
            visited[i] = True
            dfs(lev + 1, word + numbers[i], max_Len, visited, numbers)
            visited[i] = False


def solution(numbers):
    answer = 0

    N = len(numbers)
    visited = [False] * N
    numbers = list(numbers)

    for i in range(1, N + 1):
        dfs(0, "", i, visited, numbers)

    ans = set(numbers)

    for a in ans:
        if is_Prime(int(a)):
            answer += 1

    return answer