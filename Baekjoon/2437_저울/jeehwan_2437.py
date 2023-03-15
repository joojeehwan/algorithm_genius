'''


https://aerocode.net/392



1. 문제의 핵심

=> 측정할 수 있는 무게의 구간을 끊기지 않게 확장

=> 이전구간과 새롭게 생긴 구간이 연속되는가?!를 판단



2. 풀이 방향

- 기존에 [1, 10]을 측정할 수 있는 상태에서 무게가 5인 무게추가 추가로 주어졌다면,

=> 기존에 측정할 수 있었던 무게에 5 만큼 더 측정할 수 있다.

=> 즉, 닫힌 구간 [1 + 5, 10 + 5]를 추가로 측정할 수 있다.

=> [1, 15] 사이의 모든 값을 측정 가능


-  기존에  [1, 5]를 측정할 수 있는 상태에서 무게가 7인 무게추가 추가로 주어졌다면,

=> 기존에 측정할 수 있었던 무게에 5만큼 더 측정할 수 있다.

=> 즉, 닫힌 구간 [1 + 7, 5 + 7]를 추가로 측정할 수 있다.

=> [6, 7]의 구간은 측정 될 수 없다.



3. 결과

누적합으로 풀기

지금까지 구간이 끊기지 않았다면, 기존 구간은 [0, E]의 형태이고, E는 지금까지 사용했던 무게추의 누적합

기존 구간이 [0, acc[i-1]]인 상태에서 무게가 weigths[i]인 무게추가 주어진 경우

기존 구간 : [0, acc[i-1]]

신규 구관 : [weights[i], acc[i]]

이 두 구간이 끊기지 않으려면, weigths[i] < acc[i-1] + 1 를 만족해야 함.



7
3 1 6 2 7 30 1
'''



N = int(input())

weights = list(map(int, input().split()))

ans = 1

# 추를 무게별로 정렬! by bubble sort

#작은 수 부터 큰 수대로 정렬
# 1 1 2 3 6 7 30

weights.sort()
# for i in range(len(weights) - 1, 0, -1):
#     for j in range(0, i):
#         if weights[j] > weights[j + 1]:
#             weights[j], weights[j + 1] = weights[j + 1], weights[j]


for weight in weights :

    if weight < ans + 1 :
        ans += weight
    else:
        break

print(ans)


# # 리스트 복사
# prefix_sum = list(weight)
#
# # 누적합
# print(prefix_sum)
#
# for i in range(0, len(prefix_sum) - 1):
#     prefix_sum[i + 1] = prefix_sum[i] + prefix_sum[i + 1]
#
# # print(prefix_sum)
#
# res = 0
# for i in range(len(prefix_sum) - 1):
#     if prefix_sum[i] < weight[i + 1]:
#         res = prefix_sum[i] + 1
#
# print(res)
# res
# 측정 할 수 없는 경우: n번 까지의 누적합보다 n+1 번째의 오름차순으로 정렬된 배열의 값이 더 클때!