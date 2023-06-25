'''

콜라 빈병 a개를 가져다 주면, 콜라 b병

총 빈병의 갯수 n


'''


def solution(a, b, n):
    answer = 0

    while n >= a:
        # 바꿔먹지 못하고 남은 콜라
        remainCoke = n % a

        # 마트에서 다시 준 콜라

        # n을 a로 나누었을 때, 몫이 0인경우
        # while문 종료
        n = (n // a) * b

        # answer에 받은 콜라 수 기록
        answer += n

        # 다음 콜라 계산을 위해 남은 콜라 할당
        n += remainCoke

    return answer