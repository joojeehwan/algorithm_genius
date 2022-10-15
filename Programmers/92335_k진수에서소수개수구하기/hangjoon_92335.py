def notate(n, k, num=''):
    while n:
        num = str(n % k) + num
        n //= k
    return num


def is_prime(num):
    if num < 2:  # 1일 때
        return 0
    for k in range(2, int(num ** 0.5) + 1):
        if not num % k:
            return 0
    return 1


def solution(n, k):
    answer = 0

    # n을 k진수로 변환하기
    num = notate(n, k)

    # 소수 판별하기
    start = 0  # 숫자 시작 위치
    temp = ''  # 새로운 숫자 저장 공간
    while start < len(num):
        i = 0  # 숫자 진행 위치(인덱스)
        while start + i < len(num):
            # 0을 만나면 종료
            if num[start + i] == '0':
                start += 1
                break
            temp += num[start + i]
            i += 1
        # 소수 판별하기
        if temp and is_prime(int(temp)):
            answer += 1
        # 다음 숫자
        start += i
        temp = ''

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(36, 3))
print(solution(3, 3))