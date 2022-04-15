


import math

T = int(input())

for tc in range(1, T + 1):

    str_list = list(input())

    N = len(str_list)

    cnt = 0
    #회문 여부 판단 => 여기선 그냥 홀수 짝수 경우 생각안했는데!

    #이거 그냥 슬라이싱으로 했어도 되었다! 괜히 코드가 더 길어졌다!
    # str_list == str_list[::-1] 이렇게 확인
    for i in range(N // 2):
        if str_list[i] == str_list[N -1 - i]:
           cnt += 1

    if cnt == N // 2:
        print("0")
    else:
        str_left = list(str_list)
        str_right = list(str_list)

        #홀수 인 경우 생각해야 함,,why?!
        for i in range(math.ceil(int(len(str_list) / 2))):
            if str_list[i]  != str_list[-(i+1)]:
                #일단 다르면 뺸다! 왼쪽 오른쪽에서!
                str_left.pop(i)
                str_right.pop(-(i+1))


                if str_left == str_left[::-1]:
                    print("1")
                    break


                if str_right == str_right[::-1]:
                    print("1")
                    break

                print("2")
                break


#투 포인터 풀이도 알아두자!


def check(left, right):

    while left < right:

        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            return False
    return True

def twopointer(left, right):

    while left < right:

        if s[left] == s[right]:
            left += 1
            right -= 1

        else:
            if check(left + 1, right) or check(left, right-1):
                return 1
            return 2
    return 0

T = int(input())

for _ in range(T):
    s = input()
    print(twopointer(0, len(s)-1))