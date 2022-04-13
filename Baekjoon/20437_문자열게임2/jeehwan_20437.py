


#default dict를 사용하지 않으면!

# letters = "dongdongfather"
#
#
# test_dict = {}
#
# for let in letters:
#     if not let in test_dict:
#         test_dict[let] = 0
#     test_dict[let] += 1
#
#
# print(test_dict)


#유사 딕셔너리 defaultdict를 사용하자!


from collections import defaultdict

def solve(str_lst):

    len_str = len(str_lst)

    #K개 있는 문자만 따로 저장,,! 
    alpha = defaultdict(list)

    for i in range(len_str):
        #str_lst에 있는 문자중에서 k개 이상 있는 문자열 을 찾는!
        if str_lst.count(str_lst[i]) >= k:
            #k개 이상있는 문자의 인덱스를 유사dict에 저장
            alpha[str_lst[i]].append(i)
            
    #k개 이상이 있는 문자가 없다면! -1
    if not alpha:
        return (-1,)
    
    
    #k개 이상 있는 문자에 대해 문자열 게임 진행
    min_str = 10000
    max_str = 0

    #k개 이상 있는 문자끼리 인덱스를 이용하여 서로간의 거리 구한다.
    for idx_lst in alpha.values():
        #리스트에서 k개 씩 뽑아서 확인해야 해서 len idx - k + 1
        for j in range(len(idx_lst) - k + 1):
            temp = idx_lst[j+k-1] - idx_lst[j] + 1

            if temp < min_str:
                min_str = temp
            if temp > max_str:
                max_str = temp

    return min_str, max_str

T = int(input())
for t in range(1, T+1):

    syntax = input().rstrip()
    k = int(input())

    print(*solve(syntax))


