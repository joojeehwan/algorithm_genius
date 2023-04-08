def solution(topping):
    answer = 0
    cnt = len(topping)
    cheolsu = dict()
    brother = dict()

    for i in range(cnt):
        top = topping[i]
        brother[top] = brother.get(top, 0) + 1

    for cut in range(cnt-1):
        now_topping = topping[cut]
        cheolsu[now_topping] = cheolsu.get(now_topping, 0) + 1
        brother[now_topping] -= 1
        if brother[now_topping] == 0:
            del brother[now_topping]
        if len(cheolsu) == len(brother):
            answer += 1

    return answer



print(solution([1, 2, 1, 3, 1, 4, 1, 2]))