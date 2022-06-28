'''


무엇을 이분탐색하는가?! 그것을 아는것이 제일 중요!

심사관에게 입국심사 하는 시간을 이분탐색 하는것이야!

가장 적게 < = > 가장 많이

'''

# n : 사람의 수
# times : 각 심사관이 사람을 심사하는데 걸리는 시간
# 우리가 구하고 싶은 것 : 모든 사람이 심사를 받는데 가장 최소의 시간

def solution(n, times):
    answer = 0

    #right는 가장 비효율적으로 심사
    # => 가장 긴 심사시간이 소요되는 심사관에게 n명 모두 심사 받는 경우

    left, right = 1, max(times) * n

    while left <= right:

        mid = (left + right) // 2

        #모든 심사관들이 mid 분동안 심사한 사람의 수
        people = 0
        for time in times:
            people += mid // time

            #사람 수보다 많아지면 당연히 멈춰야 한다.
            if people >= n:
                break

        # 한 심사관에게 주어진 시간을 줄여본다.
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid -1

        elif people < n:
            left = mid + 1

    return answer
        


