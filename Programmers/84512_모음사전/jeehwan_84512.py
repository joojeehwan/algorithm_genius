#1. for문을 사용해서
def solution(word):
    answer = 0
    alpha  = ["A","E","I","O","U",""]
    ans = []
    for i in alpha:
        for j in alpha:
            for k in alpha:
                for l in alpha:
                    for m in alpha:
                        w = i+j+k+l+m
                        if w not in ans:
                            ans.append(w)
    ans.sort()
    answer = ans.index(word)
    return answer


#2. product 사용

from itertools import product


def solution(word):
    answer = []
    lst = ["A", "E", "I", "O", "U"]
    for i in range(1, 6):
        for li in product(lst, repeat=i):
            # print(li) 문제에서 원하는 것들을 뽑을 수 있다.
            answer.append("".join(li))  # join을 활용해서 문자열로 합친다.
    # aeiou의 순서대로 니깐 알파벳! 그냥 sort 하면된다.

    answer.sort()


#3. 재귀 사용
def solution(word):
    answer = 0

    word_lst = []
    words = ["A", "E", "I", "O", "U"]

    def dfs(cnt, word):
        if cnt == 5:
            return

        for i in range(len(words)):
            word_lst.append(word + words[i])
            dfs(cnt + 1, word + words[i])

    return word_lst.index(word) + 1