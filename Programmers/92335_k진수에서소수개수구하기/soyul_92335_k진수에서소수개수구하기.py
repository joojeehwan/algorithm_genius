def solution(n, k):

    # n을 k진수로 바꾸는 함수
    def change(n, k):
        num = ''
        while n > 0:
            num = str(n % k) + num
            n //= k
        return num

    num = change(n, k)
    num = num.split('0')            # 0을 기준으로 나눠줌

    # 소수인지 체크하는 함수
    def check(m):
        if m == 1:
            return 0
        elif m == 2:
            return 1
        else:
            for i in range(2, int(m**0.5)+1):
                if m % i == 0:
                    return 0
            return 1

    answer = 0
    for m in num:
        if len(m) == 0:
            continue
        if check(int(m)):           # 하나씩 소수인지 체크
            answer += 1

    return answer