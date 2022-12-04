

'''

길이를 target 으로 하자!

랜선의 최대 길이를 출력하는 것이니..! end가 답이 되어야 하는군

'''
K, N = map(int, input().split())

# lst = []
#
# for _ in range(K):
#     temp = int(input())
#     lst.append(temp)


#lst = list(map(int, input()) for _ in range(K)) #이렇게 하면, map obj가 들어가
lst = [int(input()) for _ in range(K)]
lst.sort()
left = 1
right = lst[-1]

while left <= right:

    mid = (left + right) // 2
    cnt = 0

    #문제를 이해했을 때의 방법 그대로...! 각각의 랜선마다, 몇개씩 나눠질 수 있나, 나눠 본거를 코드로...!
    for line in lst:
        cnt += line // mid #분활 된 랜선의 갯수

    if cnt >= N: # 길이를 너무 짧게 잡아서, target보다 더 많이! => 길이를 증가 시켜야 함.
        left = mid + 1

    else: #길이를 너무 길게 잡아서, 목표가 되는 target보다 더 적게 n개를 만든것! => 길이를 감소 시켜야 함.
        right = mid - 1


print(right)