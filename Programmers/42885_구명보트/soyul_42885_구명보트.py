# 투포인터 이용
def solution(people, limit):

    people.sort(reverse=True)

    answer = 0

    left = 0
    right = len(people) - 1

    while left < right:
        if people[right] + people[left] <= limit:           # 구명보트에 두명을 태울 수 있다면 태우고 포인터 이동
            left += 1
            right -= 1
        else:                                               # 아니면 한명만 이동
            left += 1

        answer += 1

        if left == right:                                   # 한명남으면 한명만태움
            answer += 1

    return answer