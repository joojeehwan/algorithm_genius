from itertools import product

# user id가 불량사용자인지 가능성을 확인하는 함수
def check(user, banned):

    for i in range(len(user)):
        if banned[i] == '*':                    # * 면 상관없으니까 continue
            continue
        if user[i] != banned[i]:                # 문자가 다르면 안되니까 return 0
            return 0
    return 1                                    # 검사가 끝나면 return 1

def solution(user_id, banned_id):

    can = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) != len(user_id[j]):         # 길이가 다르면 어차피 안되는거니까
                continue
            if check(user_id[j], banned_id[i]):              # 불량사용자가 맞으면 후보에 넣어둠
                can[i].append(user_id[j])

    lst = []
    pd = list(product(*can))                            # [['frodo', 'fradi'], ['abc123']] > [('frodo', 'abc123'), ('fradi', 'abc123')]
    for p in pd:
        if len(set(p)) != len(banned_id):                       # 중복된 게 있다면
            continue
        if sorted(p) in lst:
            continue
        lst.append(sorted(p))

    return len(lst)