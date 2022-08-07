'''

ㅇㅏ니 이거 정리하면서 봐버려서
그냥 눈감고 품,,ㅈㅅㅈㅅ


'''


def solution(s):
    answer = True
    arr = []

    for i in s:
        if i == "(":
            arr.append(i)

        else:
            if arr == []:
                answer = False
                break

            else:
                # 정상적이니 뺴자
                arr.pop()

    # for문을 다 돌고도 안에 값이 있으면! 뭔가 짝이 안맞는 것!
    if arr != []:
        answer = False
    return answer