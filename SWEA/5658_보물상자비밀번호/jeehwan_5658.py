'''

다시 원점 돌아올떄까지 N // 4 개씩 잘라서 확인(한 면을 본다)
같은거 있으면 set으로 해서 뺴버리자 아싸리 그냥 list에다가 넣을떄!

시계방향 회전하는거는 POP으로 뺴고 다시 insert로 앞에다가 넣어버리자! 한번 돌리는 거!


'''


T = int(input())

for tc in range(1, T+ 1):

    N, K  = map(int, input().split())
    #숫자 한개씩 담는다!
    numbers = list(map(str, input()))
    # print(numbers)
    lst = []
    for i in range(N//4): #한변에 있는 숫자의 갯수 만큼,, 다시 원점까지
        #한번 회전 => 이 문제의 포인트!
        temp = numbers.pop()
        numbers.insert(0,temp)
        for j in range(0, N, N//4): #한변에 있는 떨어져있는 숫자들을 하나의 숫자로 봐보자!
            num = ""
            for k in range(j, j + N//4):
                num += numbers[k] #문자라서 가능!
            lst.append(num)
    set_lst = set(lst) #중복 x
    # print(set_lst)
    ans_list = [] #십진수 변환한거 담긴다!
    for num in set_lst:
        ans_list.append(int(num, 16))
    ans_list.sort(reverse=True)
    # print(ans_list)
    print("#{} {}".format(tc, ans_list[K-1]))
'''
1
12 10
1B3B3B81F75E

'''