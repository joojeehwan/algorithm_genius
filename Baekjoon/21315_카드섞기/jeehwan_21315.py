'''


2번의 (2, k)- 섞기 이다! 1번만 하는게 아니라!


가능한 모든 K의 쌍에 대해 검사하여, K의 쌍으로 섞은 카드가 입력과 같다면,,?!
다시 말하면,
가능한 모든 k의 쌍에 대해 검사하여 k의 쌍으로 섞은 카드가 입력과 같다면 k의 쌍을 순서대로 출력하면 된다.

https://dongdongfather.tistory.com/72

와 모르겟어,, 이건 
'''


from collections import deque

N = int(input())
final = list(map(int, input().split()))

#완전탐색

def calc(cards, K):
    # 첫번째 단계
    _cards = deque([])
    for i in range(2**K):
        _cards.appendleft(cards.pop())
    # 이후
    for i in range(2, K+2):
        _cards2 = deque([])
        for j in range(2**(K-i+1)):  # 카드를 앞으로 뺀다.
            _cards2.appendleft(_cards.pop())
        for _ in range(len(_cards)):
            cards.appendleft(_cards.pop())
        _cards = _cards2
    for i in range(len(_cards)):
        cards.appendleft(_cards.pop())

for i in range(1, N + 1):
    if 2 ** i > N:
        break
    else:
        k = i

for i in range(1, k + 1):
    for j in range(1, k + 1):
        temp = deque([i for i in range(1, N+1)]) #초기상태 만듬
        calc(temp, i)
        calc(temp, j)
        if list(temp) == final:
            print(i, j)
            exit()