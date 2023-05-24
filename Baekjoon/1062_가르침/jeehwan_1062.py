'''

만일 K가 5 이상이라면 총 21개 중 K - 5개를 뽑는 조합의 경우와 같다.

언제나 헷갈리는 비트 마스킹 풀이
'''
from itertools import combinations

n , m = map(int, input().split())

words = [0] * n

for i in range(n) :

    temp = input()

    for word in temp :

        # |= : or 연산 후에 word[i]에 할당
        # 1 << (ord(word) - ord('a')) :  두 값의 차이만큼의 해당하는 자릿수에 찾아가, 그 자리를 1로만 바꿈(원소 추가)
        # int로 넣기에 값이 이상해 보임. 그러나 bin으로 값을 바꿔 보면, 해당 알파벳에 맞는 자리에만 값이 '1'로 되어 있음.
        debug = 1
        words[i] |= (1 << (ord(word) - ord('a')))

if m < 5 :

    print(0)

else:

    # 집합ßßßß
    first_word = {'a', 'n', 't', 'i', 'c'}
    # 집합끼리의 차집합 연산 => 나머지 알파벳 구함.
    remain_alpha = set(chr(i) for i in range(97, 123)) - first_word

    #print(remain_alpha)

    #경우의 수 구하기 (조합)

    for candi in list(combinations(remain_alpha, m - 5)):
        print(candi)