def solution(brown, yellow):
    answer = []
    total = brown + yellow  # a * b = total
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:  # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [a, b]

    return answer

'''
a  = 가로 길이 

b = 세로 길이

a >= b
2a -2b - 4 = 브라운의 갯수

(a-2) * (b-2) = 옐로우 갯수


2a + 2b = 브라운의개수 + 4
ab - 2a - 2b +4 = 옐로우 갯수

ab - brown -4 + 4 = yellow의 갯수
ab = yellow + brown


'''