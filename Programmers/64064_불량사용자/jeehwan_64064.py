from itertools import permutations


def check(users, banned_id):
    # 이중 포문을 사용해서! 밖의 i는 ()에서, 인덱스로 하나씩 고르고, j는 그거 하나 인덱스 중에서 글자의 갯수를 탐색
    # (asdf,asdfa ,asdfasdf) => 하나 고르고, "a", "s", "d", "f"를 보는 것!


    de = 1
    # users는 하나의 튜플 조합하나!
    # 답이 될 수 있는 후보들 중에 하나인데!
    # 이것이 일단은 banned_id에 있는 거랑 길이만 다르면 일단 다른 글자니깐 out처리!
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        # j는 후보로 들어오는 튜플에 한 글자의 길이!
        for j in range(len(users[i])):
            # 불량사용자 중에 하나씩 보면서 *가 나오면 pass한다. 이건 넘기고 글자 하나씩 본다!
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                # 현재 후보로 들어온 튜플이 불량사용자랑 다르다!
                return False

    return True


def solution(user_id, banned_id):
    user_permutaions = list(permutations(user_id, len(banned_id)))

    # print(user_permutaions)

    banned_set = []

    for users in user_permutaions:
        # 하나의 튜플과 비교 시작
        # 순열들의 조합중에 후보가 값이 아니면! 일단 pass 다음 경우의 수를 보자!
        if not check(users, banned_id):
            continue

        else:
            # 중복 제거!
            # 순열이라서 중복이 있으니깐! set로 중복을 제거한다!
            users = set(users)
            if users not in banned_set:
                banned_set.append(users)

    return len(banned_set)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])



#product풀이
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]

# from itertools import product
#
# def check(x, y): # banned_id, user_id를 비교
#     result = True
#     for i in range(len(x)):
#         if x[i] == '*':
#             continue
#         else:
#             if x[i] == y[i]:
#                 continue
#             else:
#                 result = False
#                 break
#
#     return result
#
#
# def solution(user_id, banned_id):
#     answer = 0
#
#     X = [] # banned_id에 해당할 수 있는 user_id를 모두 저장
#     for i in banned_id: # banned_id에서 하나
#         A = []
#         for j in user_id: # user_id에서 하나 뽑기
#             if len(i) == len(j) and check(i, j) == True: # 둘의 길이가 같고 check이 맞다면
#                 A.append(j) # A에 저장
#         X.append(A)
#
#     result = set() # 최종적으로 가능한 조합들
#     pro = list(product(*X)) # product 함수 -> X에 있는 리스트에서 각각 하나씩 뽑아 조합 리스트를 만듦
#
#     for i in pro:
#         i = list(i)
#         if len(set(i)) == len(banned_id): # 조합에서 중복을 제거(set())했을 때 길이가 같으면
#             result.add(tuple(sorted(i))) # result에 add
#     answer = len(result)
#
#     return answer


# print(solution(user_id, banned_id))

#dfs 풀이

def dfs(sj, user_id, banned_id, visit_u, visit_b, stack):
    if len(set(stack)) == len(banned_id):
        answer.append(stack[:])
        return

    for i in range(len(user_id)):
        for j in range(sj, len(banned_id)):
            if not visit_u[i] and not visit_b[j]:
                length_ui = len(user_id[i])
                length_bi = len(banned_id[j])

                if length_ui != length_bi:
                    continue

                isSame = True
                for k in range(length_ui):
                    if user_id[i][k] != banned_id[j][k]:
                        if banned_id[j][k] != "*":
                            isSame = False
                            break

                if isSame:
                    visit_b[j] = visit_u[i] = True
                    stack.append(user_id[i])
                    DFS(j, user_id, banned_id, visit_u, visit_b, stack)
                    visit_b[j] = visit_u[i] = False
                    stack.pop()


def solution(user_id, banned_id):
    global answer

    answer = []

    visit_u = [False] * len(user_id)
    visid_b = [False] * len(banned_id)
    stack = []

    # dfs

    return


