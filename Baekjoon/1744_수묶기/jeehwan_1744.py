'''


정렬을 이용

1. 양수는 큰 양수끼리

2. 음수는 작은 음수끼리 묶어 곱하기

3. 1은 무조건 더 해주는 것이 더 큰 수를 만들고,

4. 0의 경우는 음수들을 다 묶고, 남은 것이 있을 때 그 떄 그 값과 묶어 최대값이 되도록 한다.

=> 남은 음수 값을 0과 곱하기 윟서, 음수 데이터 배열에 넣어준다
=> 가장 끝에 배치 되므로, 0이 남으면 더해지고, 남는 음수값이 생기면 자동으로 곱해서 더한다.

'''


'''

4
-1
2
1
3

'''

n = int(input())

over_zero = []

under_zero = []

ans = 0

for _ in range(n):

    temp = int(input())

    if temp > 1 :
        over_zero.append(temp)
    #0인 경우 포함
    elif temp <= 0:
        under_zero.append(temp)
    #1인 경우 무조건 더하는 것이 가장 값을 크게 해줌.
    else:
        ans += temp

# for문을 사용해 앞에서부터 값을 뽑아낸다고 가정했을 시에
over_zero.sort(reverse=True)  # ex)  3,  2,  1    내림 차순 정렬
under_zero.sort()             # ex) -3, -2, -1    오름 차순 정렬
#양수 계산

# 2개씩 묶음 계산을 위해, 2칸 씩 이동
for index in range(0, len(over_zero), 2):

    # 두 개씩 묶이지 못하고, 남는 것들 처리
    if index + 1 >= len(over_zero):
        ans += over_zero[index]

    # 묶임 처리 => 곱해서 더한다.
    else:
        ans += (over_zero[index] * over_zero[index + 1])
        

#음수 계산

for index in range(0, len(under_zero), 2):

    # index + 1을 통해 조건을 거는 이유?!
    # > 2개씩 볼 때, 생기는 index 에러를 해결하기 위해, 남는 것을 볼 때
    if index + 1 >= len(under_zero):
        ans += under_zero[index]

    else:
        ans += (under_zero[index] * under_zero[index + 1])

print(ans)