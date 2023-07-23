def solution(ingredient):
    lst = []
    # print(lst[::-1])
    # print(lst[-4:])
    answer = 0
    for target in ingredient:

        lst.append(target)

        # 뒤에서 부터 시작하는 4개의 단위만 보고싶다?!
        if lst[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                lst.pop()

    return answer