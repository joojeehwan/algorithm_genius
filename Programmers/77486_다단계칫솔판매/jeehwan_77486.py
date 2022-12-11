import math


def solution(enroll, referral, seller, amount):
    # 와 이걸 이렇게 이쁘게 싸악 - zip 정리
    parent = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for _ in range(len(enroll))]))
    # print(parent)

    for i in range(len(seller)):

        money = amount[i] * 100
        target = seller[i]

        while True:
            if money < 10:
                answer[target] += money
                break

            else:
                answer[target] += math.ceil(money * 0.9)
                if parent[target] == '-':
                    break
                money = math.floor(money * 0.1)
                target = parent[target]

    return list(answer.values())


# 유니온 파인드 개념 도입


def find(parents, money, number, answer):
    # 민호까지 돈이 들어오거나 줄 돈이 없으면 종료
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)  # 총 사람 수(민호 포함 X)
    answer = [0] * (n + 1)  # 민호 포함
    d = {}  # 이름-번호의 key-value를 가지는 딕셔너리
    parents = [i for i in range(n + 1)]  # 각자 자신을 부모로 초기화
    # 이름-번호로 딕셔너리에 저장
    for i in range(n):
        d[enroll[i]] = i + 1
    # 추천인 입력
    for i in range(n):
        if referral[i] == "-":  # 민호가 추천인
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    # 칫솔 정산
    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]