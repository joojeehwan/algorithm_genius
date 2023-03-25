'''

모을 수 있는 에너지의 최댓값

N개의 에너지 구슬이 일렬로 놓여져 있고, 에너지 구슬을 이용해서 에너지를 모으려고 함.


1. 에너지 구슬 하나를 고름. -> 고른 에너지 구슬의 번호를 x라고 함. / 0번쨰와 N번째 구슬은 고를 수 없음.

2. x번째 에너지 구슬을 제거

3. x - 1 / x + 1 에너지를 모을 수 있다.

4. 전체 N을 감소 시키고, 에너지 구슬을 다시 처음부터 1 ~ N까지로 다시 번호를 매김.


'''


# 3 <= N <= 10
#


def dfs(SUM):

    global ans
    #base 조건
    if len(weights) == 2:
        ans = max(ans, SUM)
        return

    else:
        #재귀 반복 부분
        for i in range(1, len(weights) - 1):

            target = (weights[i-1] * weights[i+1])
            #구슬을 제거 했다가, 다시 넣어야 그 다음 재귀를 돌 때 원복을 시킬 수 있음.
            weight = weights.pop(i)
            dfs(SUM + target)
            weights.insert(i, weight)

N = int(input())

weights = list(map(int, input().split()))

ans = 0
dfs(0)
print(ans)