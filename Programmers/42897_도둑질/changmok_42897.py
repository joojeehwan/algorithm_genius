def solution(money):
    n = len(money)
    d = [0] * n
    max1 = 0
    max2 = 0

    d[0] = money[0]
    d[1] = money[0]

    for i in range(2, n-1):
        d[i] = max(d[i-2] + money[i], d[i-1])

    max1 = d[n-2]

    d[0] = 0
    d[1] = money[1]

    for i in range(2, n):
        d[i] = max(d[i-2] + money[i], d[i-1])

    max2 = d[n-1]

    return max(max1, max2)