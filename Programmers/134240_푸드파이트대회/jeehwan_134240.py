'''
- 더 작은 수의 숫자가, 극단으로 갈 수 있도록

- 0을 기준으로 대칭 되게

- 짝수개만 성립 가능.

'''

def solution(food):

    answer = ""

    for i, value in enumerate(food) :

        if i == 0 :
            continue

        length = value // 2

        answer += str(i) * length

    reverse = '0' + answer[::-1]

    answer += reverse

    return answer