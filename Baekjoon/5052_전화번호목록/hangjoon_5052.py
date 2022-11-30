import sys


# Testcase
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    # 전화번호 수
    pn_cnt = int(sys.stdin.readline())
    # 전화번호 리스트
    pn_lst = [sys.stdin.readline().strip() for i in range(pn_cnt)]
    # 정렬
    pn_lst.sort()
    # print(pn_lst)

    for i in range(pn_cnt-1):
        if len(pn_lst[i+1]) > len(pn_lst[i]): # i+1번째 문자열이 길이가 더 길고
            if pn_lst[i+1][:len(pn_lst[i])] == pn_lst[i]: # i번째 문자열로 시작한다면
                print('NO')
                break
    else:
        print('YES')