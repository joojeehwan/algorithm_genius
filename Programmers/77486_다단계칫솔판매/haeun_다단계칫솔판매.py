def solution(enroll, referral, seller, amount):
    answer = []

    people_cnt = len(enroll)
    sell_cnt = len(seller)

    money = dict()  # 멤버별 수익을 저장할 dict
    refer = dict()  # 멤버별 추천인을 저장할 dict

    for person_idx in range(people_cnt):
        name = enroll[person_idx]
        money[name] = 0
        refer[name] = referral[person_idx]

    for sell_idx in range(sell_cnt):
        revenue = amount[sell_idx] * 100
        person = seller[sell_idx]

        while revenue:
            if revenue >= 10:
                # 추천인에게 분배 가능
                revenue_ref = revenue // 10
                money[person] += (revenue - revenue_ref)
                revenue = revenue_ref
                person = refer[person]
                if person == "-":
                    break
            else:
                # 추천인에게 분배 불가
                money[person] += revenue
                revenue = 0

    for name in enroll:
        answer.append(money[name])

    return answer



print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))