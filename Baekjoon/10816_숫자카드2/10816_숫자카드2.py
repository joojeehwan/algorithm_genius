
'''

** 문제 **

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.


** 입력 **

첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.

둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.

넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

'''

# 이분탐색이란?!

# 정렬된 자료(오름차순)를 반으로 나누어 탐색하는 방법

# def binary_search(target, data) :
#     data.sort()
#     start, end = 0, len(data) - 1
#
#     while start <= end:
#
#         mid = (start + end) // 2
#
#         if data[mid] == target :
#             return mid
#
#         elif data[mid] < target :
#             start = mid + 1
#
#         else:
#             end = mid - 1
#
#     return None
#
# # 테스트용 코드
# if __name__ == "__main__":
#
#   li = [i**2 for i in range(11)]
#
#   target = 9
#
#   idx = binary_search(target, li)
#
#   if idx:
#       print(li[idx])
#   else:
#       print("찾으시는 타겟 {}가 없습니다".format(target))
#
# # data는 오름차순으로 정렬된 리스트
# def binary_search_recursion(target, start, end, data):
#
#     if start > end:
#         return None
#
#     mid = (start + end) // 2
#
#     if data[mid] == target:
#         return mid
#
#     elif data[mid] > target:
#         end = mid - 1
#
#     else:
#         start = mid + 1
#
#     return binary_search_recursion(target, start, end, data)
#
# # 테스트용 코드
# if __name__ == '__main__':
#
#     li = [i*3 for i in range(11)]
#
#     target = 6
#
#     idx = binary_search_recursion(target, 0, 10, li)
#
#     print(li)
#     print(idx)


N = int(input())

LST = list(map(int, input().split()))

LST.sort()

print(LST)

M = int(input())

TARGET = list(map(int, input().split()))

#print(TARGET)

def lowerBound(cards, target):

    left = 0
    right = len(cards) - 1

    while left < right:

        mid = (left + right) // 2

        if cards[mid] >= target :
            right = mid + 1

        else:
            left = mid + 1

    return left

def upperBound(cards, target):

    left = 0
    right = len(cards) - 1

    # = 이 있으면, 맞고, 없으면 틀린다,, 왜 그런거자!?
    while left <= right:

        debug = 1

        mid = (left + right) // 2

        if cards[mid] <= target :
            left = mid + 1

        else:
            right = mid -1

    return left
# 결론, 오른쪽 극단에 있는 곳에 있는 값의 초과하는 인덱스를 구하기 위해서, left <= right를 하고,
# left <= right 를 하면서, 왼쪽 극단에 있는 존재하는 값의 인덱스를 구할 때, left가 right랑 항상 같아 지는 경우가 존재한다. 이를 방지 해 while문을 종료시키기 위해 right에 -1을 한다.


for i in range(M):
     print(upperBound(LST, -10) - lowerBound(LST, TARGET[i]), end = " ")

print()

for i in range(M):
     print(upperBound(LST, -10), end = " ")

print()

for i in range(M):
     print(lowerBound(LST, TARGET[i]), end = " ")