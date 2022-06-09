def solution(money):
    house_cnt = len(money)
    dp_first = [0] + money[:house_cnt-1]
    dp_last = [0] + money[1:]

    for now in range(2, house_cnt):
        # 첫 번째 집을 선택한 경우
        dp_first[now] = max(dp_first[now-1], dp_first[now-2]+dp_first[now])
        # 마지막 집을 선택한 경우
        dp_last[now] = max(dp_last[now-1], dp_last[now-2]+dp_last[now])

    return max(dp_first[house_cnt-1], dp_last[house_cnt-1])


print(solution([91,90,5,7,5,7]))