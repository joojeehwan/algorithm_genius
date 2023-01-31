'''

그리디

문제

N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

문제 입력

첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.


예제입력

4 2
1924

예제출력

94




무조건 앞에서부터 작은 수들을 뺴면되나?! => 3번 테케 안맞음

숫자의 순서는 바뀌지 않는다.

https://yuna0125.tistory.com/52?category=1261068 참고

'''


import sys


input = sys.stdin.readline


n, k = map(int, input().split())

stack = []

numbers = list(input())

for i in range(n):
    # 앞에서부터 스택에 주어진 숫자를 하나씩 집어 넣으면서
    # 스택에 가장 최근에 들어온 값과 새로 들어온 값을 비교 => 스택에 들어있는 값이 더 작으면 pop
    while k > 0 and stack and stack[-1] < numbers[i]:
        stack.pop()
        k -= 1

    stack.append(numbers[i])


answer = ""
# 와 이렇게 하면 시간초과
# for i in stack:
#
#     answer += i
#
# print(answer)


print(''.join(stack[:len(stack)-k]))


'''

** 마지막에 출력할 때 간과했던 부분이 있는데 for문을 다 돌고 나왔음에도 k 값이 0 이상일 경우가 발생할 수 있다.
이럴 경우엔 앞에서부터 len(stack)-k 까지 출력해줘야 하는데, 여기서 처음에 n-k로 계속 작성해서 틀렸었다. 나는 k를 대체할 다른 변수를 두지 않고
k 값 그 자체에서 --를 했기 때문에 마지막에 뺄 때 온전한 k의 값이 아닌 남아있는 k 값을 빼는 것이기 때문에! 남아 있는 스택의 길이 중에서 k를 빼줘야 하는 것이었다..!!

'''