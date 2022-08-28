def solution(people, limit):
    boat = []
    answer = 0
    sorted_people = sorted(people, reverse=True)

    for pe in sorted_people:
        if sum(boat) < limit:
            boat.append(pe)
            sorted_people.pop()
            continue
        answer += 1

    return answer


'''

투 포인터를 활용한 풀이.

=> 가장 몸무게가 많이 나가는 사람과, 적게 나가는 사람을 계속해서 매칭!
최대한 한번에 태워보내면, 최소값을 찾아줄 수 있다.

사람을 최대한 많이 태워 보낼 수록 보트의 수를 적게 쓸테니!

start와 end의 값의 합이 limit을 넘지 않으면, 한번에 태워 보낸다!
만약 리미트를 넘게 되면, 무거운 사람을 태워 보낸다(작은 사람은 또 다른 사람이랑 타서 limit를 안넘을 수 있으니)

'''


def solution(people, limit):
    answer = 0
    people.sort()
    print(people)

    # start보다 end는 언제나 항상 크다!
    start, end = 0, len(people) - 1

    while start <= end:
        answer += 1
        # 정렬을 했기 때문에 이게 가능한 것!
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return answer



#함수로 빼버리기


