'''

만일 K가 5 이상이라면 총 21개 중 K - 5개를 뽑는 조합의 경우와 같다.

'''

# https://peisea0830.tistory.com/35
#비트 마스킹 풀이  => 콤비네이션
from itertools import combinations

n , m = map(int, input().split())

words = [0] * n

answer = 0

for i in range(n) :

    temp = input()

    for word in temp :

        # |= : or 연산 후에 word[i]에 할당
        # 1 << (ord(word) - ord('a')) :  두 값의 차이만큼의 해당하는 자릿수에 찾아가, 그 자리를 1로만 바꿈(원소 추가)
        # int로 넣기에 값이 이상해 보임. 그러나 bin으로 값을 바꿔 보면, 해당 알파벳에 맞는 자리에만 값이 '1'로 되어 있음.

        words[i] |= (1 << (ord(word) - ord('a')))

debug = 1
if m < 5 :

    print(0)

else:

    # 집합
    first_word = {'a', 'n', 't', 'i', 'c'}
    # 집합끼리의 차집합 연산 => 나머지 알파벳 구함.
    remain_alpha = set(chr(i) for i in range(97, 123)) - first_word

    #print(remain_alpha)

    #경우의 수 구하기 (조합)

    for candi in list(combinations(remain_alpha, m - 5)):
        print(candi)

        res = 0
        target = 0

        for word in first_word :
            target |= (1 <<(ord(word) - ord('a')))

        for word in candi:
            target |= (1 << ord(word) - ord('a'))

        # 문제에 주어진 입력과, 내가 만든 단어 비교
        for word in words :
            if target & word == word:
                res += 1

        if answer < res:
            answer = res

print(answer)
#https://kyun2da.github.io/2020/09/26/teaching/
#정석 풀이 dfs