'''


오늘 이분탐색 졸업식...

1654 랜선자르기에 이어서


'''







# A = [[0] * (N + 1) for _ in range(N + 1)]
#
# B = [0]
#
#
# for row in range(N + 1):
#     for col in range(N + 1):
#
#         if row == 0 or col == 0:
#             continue
#         A[row][col] = row * col
#         B.append(row*col)
#
# # 여기서 이분탐색으로 정렬을 하라는 건가?!
# B.sort()
#
# print(B[K])


# 와 이분탐색인거 알고 봐도 위처럼 푸네 메모리랑 시간을 봐라!! 위에처럼 하면 되겠니?!

'''

우리는 이분 탐색으로 어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지 알아낼 것이다.

A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.(너무나 당연)

예를 들어 10 * 10에서 20보다 작거나 같은 수를 생각해보자.

1*1~1*10

2*1~2*10

3*1~3*6

.

.

.

10*1~10*2

위 수가 존재할텐데, 이는 반대로 생각해보면 20을 행으로 나눈 몫이다.

20//1: 10개 --> 단 열의 숫자(N*N배열이므로)를 초과할 수 없다.

20//2: 10개

20//3: 6개

.

.

.

20//10: 2개

따라서 이를 식으로 표기해보면 아래와 같다.

temp = 0

for i in range(1, N+1):
        temp += min(mid//i, N)

 

이렇게 해당 숫자(mid)보다 작거나 같은 숫자들을 전부 찾아줌으로써 mid가 몇번째에 위치한 숫자인지 알아낼 수 있다.

이를 이분탐색으로 진행한다.

https://claude-u.tistory.com/449



'''

N = int(input())

K = int(input())

left = 1
right = K

while left <= right :
    mid = (left + right) // 2

    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)

    if temp >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)




