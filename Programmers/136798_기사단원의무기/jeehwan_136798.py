#최적환 된 약수 구하기


def measure(n):
    '''어떤 수 n 에 대한 약수를 구합니다. '''
    measure_ilst = [n]

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            measure_ilst.append(i)
            measure_ilst.append(n//i)


    return sorted(list(set(measure_ilst)))


'''
자신의 번호의 약수의 갯수의 공력을 가진 무기 구매 

단, 제한 수치보다 더 큰 약수의 갯수 => 정해진 공력을 가지는 무기 구매 


1 ~ number 의 수 중에서, 

'''


def solution(number, limit, power):
    answer = 0

    def solve(num):
        cnt = 0
        nonlocal answer
        for i in range(1, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                if i == num // i:  # 제곱근일 경우 -> 1개만 카운트하기
                    cnt += 1
                else:
                    cnt += 2  # 제곱근이 아닐 경우, 2개 카운트 (i, n//i)
            # print("약수의 갯수", cnt)
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    for i in range(1, number + 1):
        solve(i)
        # print(i, answer)
    return answer

print(measure(36))

#제곱근인 경우에는 +1을 더해서 +2 를 하도록 if를 중첩
def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                # 제곱근이 아닌 경우에는 +1을 더해서 +2 를 하도록 if를 중첩
                if i // j != j:
                    count += 1

            if count > limit:
                break

        if count > limit:
            answer += power
        else:
            answer += count



    return answer